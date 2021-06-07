import pymysql
import config

'''
- MySQL DB 연결
- DB와 상호작용하기 위한 cursor 객체 생성
return : DB 접근을 위한 cursor 객체와 conn
'''


def connectDB():
    conn = pymysql.connect(
        user='root',
        passwd=config.DB_PASSWORD,
        host='127.0.0.1',
        db=config.DB_DATABASE,
        charset='utf8'
    )
    cursor = conn.cursor()

    return cursor, conn


cursor, conn = connectDB()

'''
- MySQL DB 조회 함수
- 주어진 용언이 이미 DB에 저장되어 있는 용언인지 판별
@param word_info : 문장을 이루는 형태소에 대한 정보 (type = tuple)
                    (형태소, 품사)로 이루어짐
return : DB 내에 해당 용언의 유무 (있을 시 TRUE, 없을 시 FALSE)
'''


def dbCheck(word_info, table):
    sql = "SELECT Wid FROM WORDS WHERE Word = %s AND Class = %s;"
    cursor.execute(sql, word_info)
    wid = cursor.fetchall()

    if table == 'WORDS':
        return wid
    elif table == 'CONVERSION':
        sql = "SELECT * FROM CONVERSION WHERE Wid = %s;"
        cursor.execute(sql,  wid)
        result = cursor.fetchall()

        return bool(result)
    elif table == 'ENGWORDS':
        sql = "SELECT * FROM ENGWORDS WHERE Wid = %s;"
        cursor.execute(sql, wid)
        result = cursor.fetchall()

        return bool(result)


'''
- MySQL DB 처리를 수행하는 함수
- 형태소 정보가 주어지면 변환이 필요한 단어를 반환하는 전체적인 DB 처리를 포함
@param word_info : 문장을 이루는 형태소에 대한 정보 (type = tuple)
                    (형태소, 품사)로 이루어짐
return : 변환이 필요한 경우 변환할 단어의 정보
'''


def dbProcess(word_info, eng_pos, Hflag):
    wid = dbCheck(word_info, "WORDS")
    if wid:     # DB에 있어?
        if dbCheck(word_info, "ENGWORDS"):      # ENGWORDS에 있어?
            for e in eng_pos:
                sql = "SELECT Conflag, Irrflag FROM ENGWORDS WHERE Wid = %s AND Eng = %s;"
                cursor.execute(sql, (wid, e))
                result = list(cursor.fetchall())
                if result:
                    result = result[0]
                    break
            if result:
                if result[0] == 1:
                    if Hflag == 1:
                        sql = "SELECT Word, PconFlag FROM WORDS, CONVERSION WHERE Hwid = %s AND Wid = Pwid;"
                        cursor.execute(sql, wid)
                        result = list(cursor.fetchall())
                    elif Hflag == 0:
                        sql = "SELECT Word, HconFlag FROM WORDS, CONVERSION WHERE Pwid = %s AND Wid = Hwid;"
                        cursor.execute(sql, wid)
                        result = list(cursor.fetchall())
                    if result:
                        result = result[0]
                        word_info[0] = result[0]
                        word_info.append(result[0])
                    else:
                        word_info.append(0)
                else:
                    result = result[0]
                    word_info.append(result[1])
                    return word_info
            else:
                word_info.append(0)
                return word_info
        else:
            if Hflag == 1:
                sql = "SELECT P.Word, P.Conjugation FROM WORDS H, WORDS P, CONVERSION WHERE H.Word = %s AND H.Wid = Hwid AND Pwid = P.Wid;"
            elif Hflag == 0:
                sql = "SELECT H.Word, H.Conjugation FROM WORDS P, WORDS H, CONVERSION WHERE P.Word = %s AND P.Wid = Pwid AND Hwid = H.Wid;"
            cursor.execute(sql, word_info[0])
            result = list(cursor.fetchall())

            if not result:
                sql = "SELECT Word, Conjugation FROM WORDS WHERE Wid = %s;"
                cursor.execute(sql, wid)
                result = cursor.fetchall()
            result = result[0]
            word_info[0] = result[0]
            word_info.append(result[1])

        if word_info[2] is None:
            word_info[2] = 0

        return word_info
    else:
        word_info.append(0)
        return word_info


'''
- 형태소 단위로 주어진 문장에서 특정 단어 변환을 수행하는 함수
- DB에서 형태소 정보를 탐색하며 필요 시 단어 변환 수행
- 불규칙 변환 처리가 필요한 경우 flag 1을 추가
@param sentence : 띄어쓰기가 처리된 [형태소, 품사]의 집합 형태의 문장
return : 단어 변환이 이루어진 후의 sentence
'''


def conversion(sentenceInfo, eng_pos):
    target = ['NNG', 'VV', 'VA', 'XSV']
    flag = 0
    for idx, symbol in enumerate(sentenceInfo[1]):
        if(symbol[1] in target):
            conv = dbProcess(symbol, eng_pos, sentenceInfo[2][0])
            if conv[2] == 1:
                flag = 1
            sentenceInfo[1][idx] = list(conv)[:-1]

    sentenceInfo[2][1] = flag
    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo
