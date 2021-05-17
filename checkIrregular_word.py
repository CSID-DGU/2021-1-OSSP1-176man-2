import hgtk
from konlpy.tag import Komoran

'''
입력받은 문장을 어절 단위로 끊어, 분석된 형태소들을 그대로 붙인 것과 입력받은 문장을 비교하여 문장 내 규칙/불규칙 활용 여부를 확인한다.
(ex. 합니다 -> 하, ㅂ니다 -> 합니다  =>  합니다 == 합니다 : 규칙)
(ex. 흘러 -> 흐르, 어 -> 흐르어  =>  흐르어 != 흘러 : 불규칙)
Return : 문장 내 규칙/불규칙 활용 여부 (문장 내 단어의 불규칙 활용 존재 여부)
'''


def checkIrregular(kor):
    komoran = Komoran()
    wordList = kor.split()

    # morphemeList = 각 어절을 형태소 분석하고 분석된 형태소를 그대로 이어 붙여 만든 어절을 저장하는 배열
    morphemeList = []
    for i in wordList:
        word = komoran.pos(i)
        z = list(map(list, word))
        tempWord = ""
        for j in range(len(z)):
            tempWord += (z[j][0])

        morphemeList.append(tempWord)

    # flag : 전체 문장 내 불규칙 활용이 있는지 여부를 체크하기 위한 flag 변수
    flag = True
    for index, i in enumerate(morphemeList):
        cnt = 0
        cntList = []
        sentWithSyllable = ""

        # 형태소 분석과정에서 자음만 있는 경우 존재(ex. 축구를합니다 -> 축구를하ㅂ니다)
        # 자음만 있는 위치를 저장
        for j in i:
            if ord('ㄱ') <= ord(j) and ord(j) <= ord('ㅎ'):
                cntList.append(cnt)
            cnt += 1

        # s : i 문자열의 모든 음절을 자모분리하여 저장한 문자열
        s = hgtk.text.decompose(i)

        # hgtk에서 음절을 ᴥ표시로 구분
        # sentWithSyllable : decomposeString 문자열에 ᴥ 기준으로 자음만 들어있는 경우를 없앤 문자열(자음만 있는 경우 그 앞 음절쪽으로 붙임)
        cnt1 = 1
        for j in s:
            if j == 'ᴥ' and cnt1 in cntList:
                cnt1 += 1
            elif j == 'ᴥ' and cnt1 not in cntList:
                sentWithSyllable += 'ᴥ'
                cnt1 += 1
            else:
                sentWithSyllable += j

        # perfectString : sentWithSyllable 문자열을 ᴥ 기준으로 자모합성하여 만든 문자열
        perfectString = hgtk.text.compose(sentWithSyllable)

        # perfectString과 입력된 원문 어절을 비교하여 문장의 규칙/불규칙 여부 판별
        if (perfectString != wordList[index]):
            flag = False
            print("불규칙 : " + wordList[index] + "->" + perfectString)

    if(flag):
        print("문장 내 불규칙 활용이 없습니다.")


kor = "강물이 흘러."
checkIrregular(kor)
