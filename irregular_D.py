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
2021-05-28 1차 수정 - 변형 조건 반영하여 수정

'''
inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence) # 문장종류 확인
sentenceInfo = naverPapago.translate(inputSentence) # 파파고API로 번역 및 Komoran으로 형태소 분석
korList = hae.hae(komoranSpacing.Spacing(sentenceInfo[1]), 'Command')
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX', 'EP']
def endmidIrregular(korList):
    for i in range(len(korList[1])):
        #ㅎ 불규칙 처리, 어미 '-아' 앞에서 ㅣ로 바뀌어 합쳐지는 활용 형식
        if korList[1][i][1] == 'EF' and korList[1][i][0] == '아' :
            for j in range(len(korList[1])):
                j=i-1 #조건문을 korList에서 거꾸로 들어가는 방법을 찾아야함
                if korList[1][j][1] in vb and hgtk.text.decompose(korList[1][j][0])[len(hgtk.text.decompose(korList[1][j][0]))-2] == 'ㅎ':
                    tmp = list(hgtk.text.decompose(korList[0][j])) 
                    tmp[len(tmp)-3] = 'ㅐ'
                    tmp[len(tmp)-2] = ''
                    korList[1][j][0] = hgtk.text.compose(tmp)
                    korList[0][j] = hgtk.text.compose(tmp)
                    korList[1][i][1] = ''
                    korList[1][i][0] = ''
                    korList[0][i] = ''
                break
        elif korList[1][i][1] == 'EF' and korList[1][i][0] == '어' :
            for j in range(len(korList[1]), 0, -1):
                if korList[1][j][1] in vb and hgtk.text.decompose(korList[1][j][0])[len(hgtk.text.decompose(korList[1][j][0]))-2] == 'ㅎ':
                    tmp = list(hgtk.text.decompose(korList[0][j])) 
                    tmp[len(tmp)-3] = 'ㅔ'
                    tmp[len(tmp)-2] = ''
                    korList[1][j][0] = hgtk.text.compose(tmp)
                    korList[0][j] = hgtk.text.compose(tmp)
                    korList[1][i][1] = ''
                    korList[1][i][0] = ''
                    korList[0][i] = ''
                break
        elif korList[1][i][1] == 'EF' and korList[1][i][0] == '아' :
            for j in range(len(korList[1]), 0, -1):
                if korList[1][j][1] in vb and hgtk.text.decompose(korList[1][j][0])[len(hgtk.text.decompose(korList[1][j][0]))-2] == 'ㅎ':
                    tmp = list(hgtk.text.decompose(korList[0][j])) 
                    tmp[len(tmp)-3] = 'ㅐ'
                    tmp[len(tmp)-2] = ''
                    korList[1][j][0] = hgtk.text.compose(tmp)
                    korList[0][j] = hgtk.text.compose(tmp)
                    korList[1][i][1] = ''
                    korList[1][i][0] = ''
                    korList[0][i] = ''
                break
    return korList
        #으 불규칙 처리, 어미 '-아' 앞에서 사라지는 활용 형식
korList = endmidIrregular(korList)
print(korList)
        
        

                    

            