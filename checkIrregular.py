import hgtk
from konlpy.tag import Komoran

'''
입력받은 문장을 형태소 분석하고 분석된 형태소들을 그대로 붙인 것과 입력받은 문장을 비교하여 문장내 규칙/불규칙 활용 여부를 확인한다.
(ex. 합니다 -> 하, ㅂ니다 -> 합니다  =>  합니다 == 합니다 : 규칙)
(ex. 흘러 -> 흐르, 어 -> 흐르어  =>  흐르어 != 흘러 : 불규칙)
Return : 문장내 규칙/불규칙 활용 여부 (문장 내 단어의 불규칙 활용 존재 여부)
'''

def checkIrregular(kor):
    komoran = Komoran()
    str = komoran.pos(kor)
    z = list(map(list, str))

    tokenList = []
    for i in range(len(z)):
        tokenList.append(z[i][0])

    #sentence : 문장을 형태소 분석하여 나온 형태소들을 붙여놓은 문자열
    sentence = "".join(tokenList)
    print(sentence)

    cnt = 0
    cntList = []

    #형태소 분석과정에서 자음만 있는 경우 존재(ex. 축구를합니다 -> 축구를하ㅂ니다)
    #자음만 있는 위치를 저장
    for word in sentence:
        if ord('ㄱ') <= ord(word) and ord(word) <= ord('ㅎ'):
            cntList.append(cnt)
        cnt += 1

    #decomposeString : sentence 문자열의 모든 음절을 자모분리하여 저장한 문자열
    decomposeString = hgtk.text.decompose(sentence)
    print(decomposeString)

    #hgtk에서 음절을 ᴥ표시로 구분
    #sentWithSyllable : decomposeString 문자열에 ᴥ 기준으로 자음만 들어있는 경우를 없앤 문자열(자음만 있는 경우 그 앞 음절쪽으로 붙임)
    sentWithSyllable = ""
    cnt = 1
    for token in decomposeString:
        if token == 'ᴥ' and cnt in cntList:
            cnt += 1
        elif token == 'ᴥ' and cnt not in cntList:
            sentWithSyllable += 'ᴥ'
            cnt += 1
        else:
            sentWithSyllable += token
    print(sentWithSyllable)

    #perfectString : sentWithSyllable 문자열을 ᴥ 기준으로 자모합성하여 만든 문자열
    perfectString = hgtk.text.compose(sentWithSyllable)
    print(perfectString)

    #perfectString과 입력된 문자열을 비교하여 문장의 규칙/불규칙 여부 판별
    if (perfectString == kor.replace(" ", "")):
        return("규칙")
    else:
        return("불규칙")

kor="축구를 합니다."
print(checkIrregular(kor))