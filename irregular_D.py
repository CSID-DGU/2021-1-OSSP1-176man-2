import hgtk
import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hae

'''
ㅎ, 으, ㄹ 에 대한 불규칙 변형 함수
불규칙이 라고 판단될 시 해당 함수를 실행시킨다.
2021-05-25 작성 시작
2021-05-25 ㅎ불규칙 초안 작성 완료, 어미마다 모음과의 합성 필요
'''
inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence) # 문장종류 확인
sentenceInfo = naverPapago.translate(inputSentence) # 파파고API로 번역 및 Komoran으로 형태소 분석
korList = komoranSpacing.Spacing(sentenceInfo[1])
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX', 'EP']

def endmidIrregular(korList):
    for i in range(len(korList[1])):
        if korList[1][i][1] == 'EF':
            if korList[1][i - 1][1] in vb:
                tmp = hgtk.text.decompose(korList[1][i - 1][1])
                #'ㅎ' 불규칙 처리
                if tmp[len(tmp) - 2] == 'ㅎ':
                    tmp[len(tmp) - 2] = ''
                    tmp[len(tmp) - 3] = ''
                #'으' 불규칙 처리
                korList[1][i - 1][1] = hgtk.text.compose(tmp)