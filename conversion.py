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


def dbCheck(word_info):
    sql = "SELECT * FROM WORDS WHERE Word = %s;"
    cursor.execute(sql, word_info[0])
    result = cursor.fetchall()

    return bool(result)


'''
- MySQL DB 처리를 수행하는 함수
- 형태소 정보가 주어지면 변환이 필요한 단어를 반환하는 전체적인 DB 처리를 포함
@param word_info : 문장을 이루는 형태소에 대한 정보 (type = tuple)
                    (형태소, 품사)로 이루어짐
return : 변환이 필요한 경우 변환할 단어의 정보
'''


def dbProcess(word_info):
    if dbCheck(word_info):
        sql = "SELECT P.Word, P.Class FROM WORDS H, WORDS P, CONVERSION WHERE H.Word = %s AND H.Wid = Hwid AND Pwid = P.Wid;"
        cursor.execute(sql, word_info[0])

        result = list(cursor.fetchall())
        if result:
            word_info = list(result[0])
    else:
        return

    sql = "SELECT Conjugation FROM WORDS WHERE Word = %s;"
    cursor.execute(sql, word_info[0])
    result = word_info + list(cursor.fetchall()[0])

    return result


'''
- 형태소 단위로 주어진 문장에서 특정 단어 변환을 수행하는 함수
- DB에서 형태소 정보를 탐색하며 필요 시 단어 변환 수행
- 불규칙 변환 처리가 필요한 경우 flag 1을 추가
@param sentence : 띄어쓰기가 처리된 [형태소, 품사]의 집합 형태의 문장
return : 단어 변환이 이루어진 후의 sentence
'''


def conversion(sentenceInfo):
    target = ['NNG', 'VV', 'VA', 'XSV']
    flag = 0
    for idx, symbol in enumerate(sentenceInfo[1]):
        if(symbol[1] in target):
            conv = dbProcess(symbol)
            if conv[2] == 1:
                flag = 1
            sentenceInfo[1][idx] = list(conv)[:-1]

    sentenceInfo.append(flag)
    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo
