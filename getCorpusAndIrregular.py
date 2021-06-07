import pandas as pd
from konlpy.tag import Komoran
import hgtk
import config
import pymysql
import vowelReduction
import copy

FILE_PATH = config.FILE_PATH  # 말뭉치 excel 파일이 위치한 경로

komoran = Komoran()


'''
- 말뭉치 excel 파일 불러오기
- 영어 문장의 길이가 250자가 넘어갈 경우 리스트에서 제외
- 원하는 범위만 리스트형태로 반환
@param fname     : excel file name (type = string)
@param start_idx : (default = 0) 받아올 리스트의 시작 index
@param idx_range : (default = 20) 받아올 리스트의 범위
return : 한국어 또는 영어 말뭉치 리스트 (type = list)
'''


def getCorpus(fname, lang, start_idx=140, idx_range=40):
    # pd.set_option('display.max_rows', None)  # row 생략 없이 출력
    # pd.set_option('display.max_columns', None)  # col 생략 없이 출력

    excelTitle = FILE_PATH + fname  # 경로 + 파일명
    excel_dafaframe = pd.read_excel(
        excelTitle + ".xlsx", engine='openpyxl')  # 원본 excel 파일
    eng_list = list((excel_dafaframe['번역문']))  # 영어 문장 (번역문)
    kor_list = list((excel_dafaframe['원문']))  # 한국어 문장 (원문)

    # datum = ['\'', '\"', ','] # 사용 x
    si = start_idx
    cnt = 0
    while True:
        # 리스트에서 원하는 range의 문장들이 찾아졌을 때, 리스트의 범위를 초과하였을 때
        if cnt > idx_range or si >= len(eng_list):
            break

        # 영어 문장이 250자를 초과할 때 리스트에서 제외
        # or any(elem in eng_list[si] for elem in datum):
        if len(eng_list[si]) > 250:
            eng_list.pop(si)
            kor_list.pop(si)
        else:
            cnt += 1
            si += 1

    if lang == 'kor':
        return kor_list[start_idx: start_idx + idx_range]
    else:
        return eng_list[start_idx: start_idx + idx_range]


'''
입력받은 문장을 어절 단위로 끊어, 분석된 형태소들을 그대로 붙인 것과 입력받은 문장을 비교하여 문장 내 규칙/불규칙 활용 여부를 확인한다.
(ex. 합니다 -> 하, ㅂ니다 -> 합니다  =>  합니다 == 합니다 : 규칙)
(ex. 흘러 -> 흐르, 어 -> 흐르어  =>  흐르어 != 흘러 : 불규칙)
@param original_text : 원본 한국어 문장 (type = string)
return : 문장 내 불규칙 활용된 형태소 리스트 (type = list)
         (ex. [(불규칙 활용된 형태소, 형태소의 품사)])
         (ex. [('아름답', 'VA')])
'''


def getIrregular(original_text):
    word_list = original_text.split()

    # stem : 각 단어의 어간을 저장하는 배열
    stem = []
    # morpheme_list : 각 어절을 형태소 분석하고 분석된 형태소를 그대로 이어 붙여 만든 어절을 저장하는 배열
    morpheme_list = []

    # irregular_stem_tag : 불규칙 활용이 가능한 품사들을 저장한 배열(동사, 형용사, 보조용언, 동사 파생 접미사, 형용사 파생 접미사)
    irregular_stem_tag = ["VV", "VA", "VX", "XSV", "XSA"]

    for i in word_list:
        word = komoran.pos(i)
        word1 = komoran.morphs(i)
        word = list(map(list, word))
        word1 = list(map(list, word1))

        r_word = copy.deepcopy(word)

        w_list = [word1, word]
        komoran_word_list = vowelReduction.vowelReduction(w_list)
        komoran_word_list = komoran_word_list[1]

        # stem_flag : 어절내에 불규칙이 가능한 용언이 있는지 여부를 파악하기 위한 flag 변수
        stem_flag = False
        # stem에 각 단어의 어간을 저장
        # 처리 방법 : 접두사를 제외하고 가장 먼저 오는 형태소
        for index in range(len(komoran_word_list)):
            if(komoran_word_list[index][1] in irregular_stem_tag):
                stem_flag = True
                stem.append(
                    (r_word[index][0], r_word[index][1]))
                break

        # 어절에 불규칙 활용이 가능한 품사가 없더라도 어절의 인덱스를 맞추기 위해 배열에 추가
        if(not(stem_flag)):
            stem.append(("NULL", "NULL"))

        tempWord = ""
        for j in range(len(komoran_word_list)):
            tempWord += (komoran_word_list[j][0])

        morpheme_list.append(tempWord)

    irregular_list = []  # 불규칙 활용이 발생한 어간들을 저장하는 배열
    indexList = []  # 불규칙 활용이 존재하는 어절의 index를 저장하는 배열
    for index, i in enumerate(morpheme_list):
        cnt = 0
        cnt_list = []
        sent_with_syllable = ""

        # 형태소 분석과정에서 자음만 있는 경우 존재(ex. 축구를합니다 -> 축구를하ㅂ니다)
        # 자음만 있는 위치를 저장
        for j in i:
            if ord('ㄱ') <= ord(j) and ord(j) <= ord('ㅎ'):
                cnt_list.append(cnt)
            cnt += 1

        # s : i 문자열의 모든 음절을 자모분리하여 저장한 문자열
        s = hgtk.text.decompose(i)

        # hgtk에서 음절을 ᴥ표시로 구분
        # sent_with_syllable : decomposeString 문자열에 ᴥ 기준으로 자음만 들어있는 경우를 없앤 문자열(자음만 있는 경우 그 앞 음절쪽으로 붙임)
        cnt1 = 1
        for j in s:
            if j == 'ᴥ' and cnt1 in cnt_list:
                cnt1 += 1
            elif j == 'ᴥ' and cnt1 not in cnt_list:
                sent_with_syllable += 'ᴥ'
                cnt1 += 1
            else:
                sent_with_syllable += j

        # perfect_string : sent_with_syllable 문자열을 ᴥ 기준으로 자모합성하여 만든 문자열
        perfect_string = hgtk.text.compose(sent_with_syllable)

        # perfectString과 입력된 원문 어절을 비교하여 문장의 규칙/불규칙 여부 판별
        if (perfect_string != word_list[index]):
            print("----")
            print(perfect_string)
            print(word_list[index])

            indexList.append(index)

    for i in indexList:
        if not stem[i] == ("NULL", "NULL"):
            irregular_list.append(stem[i])

    return irregular_list


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


'''
- MySQL DB 삽입, 변경 함수
- 불규칙 용언에 해당하는 단어의 어간을 처리하기 위한 DML
@param cursor, conn : DB 연결 시 반환받은 cursor 객체와 conn
@param word_info : 처리를 통해 분류한 불규칙 용언에 대한 정보 (type = tuple)
                    (용언의 어간, 품사)로 이루어짐
'''


def dbInsert(cursor, conn, word_info):
    sql = "INSERT INTO WORDS(Word, Class, Conjugation) VALUES (%s, %s, 1);"
    cursor.execute(sql, word_info)
    conn.commit()


def dbUpdate(cursor, conn, word_info):
    sql = "UPDATE WORDS SET Conjugation = 1 WHERE Word = %s"
    cursor.execute(sql, word_info[0])
    conn.commit()


'''
- MySQL DB 조회 함수
- 주어진 용언이 이미 DB에 저장되어 있는 용언인지 판별
@param cursor : DB 연결 시 반환받은 cursor 객체
@param word_info : DB에 존재하는 지 판별할 용언에 대한 정보 (type = tuple)
                    (용언의 어간, 품사)로 이루어짐
return : DB 내에 해당 용언의 유무 (있을 시 TRUE, 없을 시 FALSE)
'''


def dbCheck(cursor, word_info):
    sql = "SELECT * FROM WORDS WHERE Word = %s AND Class = %s;"
    cursor.execute(sql, word_info)
    result = cursor.fetchall()

    return bool(result)


'''
- MySQL DB 처리를 수행하는 함수
- 불규칙 용언의 정보가 주어지면 DB에 삽입 또는 변경하기 위해 이루어지는 전체적인 DB 처리를 포함
@param word_info : DB에 존재하는 지 판별할 용언에 대한 정보 (type = tuple)
                    (용언의 어간, 품사)로 이루어짐
'''


def dbProcess(word_info):
    cursor, conn = connectDB()
    print(word_info)
    if not dbCheck(cursor, word_info):
        dbInsert(cursor, conn, word_info)
    else:
        dbUpdate(cursor, conn, word_info)


def eliminate(irregular_list):
    print("삭제할 인덱스를 입력하세요(없다면 -1 입력) : ")
    index = int(input())
    while(index != -1):
        del irregular_list[index]
        print("========")
        print(irregular_list)
        print("========")
        print("삭제할 인덱스를 입력하세요(없다면 -1 입력) : ")
        index = int(input())

    return irregular_list


'''
- 불규칙 용언 판별
- getCorpus()를 통해 말뭉치 파일을 읽어들임
- getIrregular()를 통해 말뭉치의 문장들에서 불규칙 용언 추출
- dbProcess()를 통해 추출한 불규칙 용언을 DB에 저장
'''


# getCorpus
original_corpus_list = getCorpus("test", 'kor')
#print("getCorpus() : ", original_corpus_list)

irregular_list = set()

# getIrregular
for i in range(len(original_corpus_list)):
    isIregular = getIrregular(original_corpus_list[i])
    for j in isIregular:
        irregular_list.add(j)

        print(i)
        print(j)
        print("----")

print("============")
print(irregular_list)
print("============")
irregular_list = list(irregular_list)
irregular_list = eliminate(irregular_list)

print(irregular_list)


for i in irregular_list:
    dbProcess(i)
