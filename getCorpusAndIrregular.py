import pandas as pd
from konlpy.tag import Komoran
import hgtk

FILE_PATH = "C:\\Users\woosu\Desktop\공소\말뭉치"  # 말뭉치 excel 파일이 위치한 경로

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


def getCorpus(fname, lang, start_idx=0, idx_range=20):
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
        komoran_word_list = list(map(list, word))

        # stem_flag : 어절내에 불규칙이 가능한 용언이 있는지 여부를 파악하기 위한 flag 변수
        stem_flag = False
        # stem에 각 단어의 어간을 저장
        # 처리 방법 : 접두사를 제외하고 가장 먼저 오는 형태소
        for index in range(len(komoran_word_list)):
            if(komoran_word_list[index][1] in irregular_stem_tag):
                stem_flag = True
                stem.append(
                    (komoran_word_list[index][0], komoran_word_list[index][1]))
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
            indexList.append(index)

    for i in indexList:
        irregular_list.append(stem[i])

    return irregular_list


''' 
example 
'''
# getCorpus
original_corpus_list = getCorpus("\\1_구어체(1)_200226", 'kor', 0, 3)
print("getCorpus() : ", original_corpus_list)

# getIrregular
for i in range(3):
    my_irregular_list = getIrregular(original_corpus_list[i])
    print("getIrregular() : ", my_irregular_list)