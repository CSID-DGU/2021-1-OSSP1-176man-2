import hgtk
import naverPapago
import komoranSpacing
import engInputAnalysis

inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence)  # 문장종류 확인
sentenceInfo = naverPapago.translate(inputSentence)  # 파파고API로 번역 및 Komoran으로 형태소 분석
korList = komoranSpacing.Spacing(sentenceInfo[1])
print(korList)


'''
'ㄷ', 'ㅂ', 'ㅅ', '르', '우' 에 대한 불규칙 변형 처리

** '르' 처리 제외 초안 작성 완료

활용되지 않은 어간일 때 활용 처리
ex) 걷(다) -> 걸(어)
ex) 가볍(다) -> 가벼(워)
ex) 긋(다) -> 그(어)
ex) 누르(다) -> 눌(러)
ex) 푸다 -> 퍼

'''


# stem_type: 불규칙 활용 처리 시 '어간'의 형태소 종류
stem_type = ['VV', 'VA', 'XR'] 

def stemIrregular(korList):

    for idx in range(len(korList[1])):
        if korList[1][idx][1] in stem_type:
            stem_decomposed = list(hgtk.text.decompose(korList[1][idx][0]))
            
            # 'ㄷ' 불규칙 활용
            if stem_decomposed[-2] == 'ㄷ':
                stem_decomposed[-2] = 'ㄹ'
                korList[1][idx][0] = hgtk.text.compose(''.join(stem_decomposed)) # + '어'

            # 'ㅂ' 불규칙 활용
            if stem_decomposed[-2] == 'ㅂ':
                stem_decomposed = stem_decomposed[:-2]
                stem_decomposed.append('ᴥ')
                korList[1][idx][0] = hgtk.text.compose(''.join(stem_decomposed)) # + '워'

            # 'ㅅ' 불규칙 활용
            if stem_decomposed[-2] == 'ㅅ':
                stem_decomposed = stem_decomposed[:-2]
                stem_decomposed.append('ᴥ')
                korList[1][idx][0] = hgtk.text.compose(''.join(stem_decomposed))  # + '어'
            
            # '르' 불규칙 활용

            # '우' 불규칙 활용
            if stem_decomposed[-2] == 'ㅜ':
                stem_decomposed[-2] = 'ㅓ'
                korList[1][idx][0] = hgtk.text.compose(''.join(stem_decomposed))






