import hgtk

'''
hgtk에 존재하는 함수를 사용해서 hgtk.letter.compose('가', 'ㅁ'), hgtk.text.compose('가ㅁ')을 실행하면 에러가 뜬다. 
따라서 형태소 분석시 '가','ㅁ'로 나누어졌을 때 이를 '감'으로 합치는 함수.
korList : komoran.morphs()으로 분석된 형태소 List
Return : 형태소 List를 하나의 문장으로 합친 String
'''


def textCompose(korList):
    cnt = 0
    cntList = []
    punctuation = ['!', '.', '?']

    korTextString = ""
    for text in korList:
        korTextString += text

    # 문자열에서 자음이 몇번째 있는지를 cntList에 넣는다. ex) 공부하면하ㄹ수록 -> cnt = 5
    for text in korTextString:
        if ord(text) <= ord('ㅎ') and text not in punctuation:
            cntList.append(cnt)
        cnt += 1

    # 문자열을 분해한다.
    decomposeString = hgtk.text.decompose(korTextString)

    cnt = 1
    inperfectString = ""

    # 분해된 문자열은 ᴥ으로 구분되어 합성됨 ex) ㅎㅏᴥㄹᴥㅅㅜ
    # 이때 cnt를 이용하여 자음만 있는 부분에 ᴥ를 삭제한다. ex) ㅎㅏㄹᴥㅅㅜ
    for txt in decomposeString:
        if txt == 'ᴥ' and cnt in cntList:
            inperfectString += ""
            cnt += 1
        elif txt == 'ᴥ' and cnt not in cntList:
            inperfectString += 'ᴥ'
            cnt += 1
        else:
            inperfectString += txt

    # 분해된 문자열을 합친다.
    perfectString = hgtk.text.compose(inperfectString)
    return perfectString


inputData = ['공부', '를', '하', '면', '하', 'ㄹ수록', '모르', '는',
             '게', '많', '다는', '것', '을', '알', '게', '되', 'ㅂ니다', '.']
print(textCompose(inputData))
