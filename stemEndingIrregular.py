import hgtk
import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hae
import haeyo

'''
ㅎ, 으, ㄹ 에 대한 불규칙 변형 함수
불규칙이 라고 판단될 시 해당 함수를 실행시킨다.
2021-05-25 작성 시작
2021-05-28 1차 수정 - 변형 조건 반영하여 수정
2021-06-01 2차 수정 - ㅎ불규칙에 대해 필요없는 부분 삭제 및 형용사 인덱스 절대값 부여, 코드 수정(해, 해요체 구분 작성)
'''
inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence) # 문장종류 확인
sentenceInfo = naverPapago.translate(inputSentence) # 파파고API로 번역 및 Komoran으로 형태소 분석
sentenceInfo = haeyo.haeyo_ver1(komoranSpacing.Spacing(sentenceInfo[1]), 'Command')
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX', 'EP']
def stemEndingIrregular(sentenceInfo):
    for i in range(len(sentenceInfo[1])):
        #ㅎ 불규칙 처리, 어미 '-아' 앞에서 ㅣ로 바뀌어 합쳐지는 활용 형식 / 해체
        if sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i][0] == '아' :
            if sentenceInfo[1][i - 1][1] in vb and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-2] == 'ㅎ' and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-3] != 'ㅑ':
                tmp = list(hgtk.text.decompose(sentenceInfo[0][i - 1])) 
                tmp[len(tmp)-3] = 'ㅐ'
                tmp[len(tmp)-2] = ''
                sentenceInfo[1][i - 1][0] = hgtk.text.compose(tmp)
                sentenceInfo[0][i - 1] = hgtk.text.compose(tmp)
                sentenceInfo[1][i][1] = ''
                sentenceInfo[1][i][0] = ''
                sentenceInfo[0][i] = ''
                break
            elif sentenceInfo[1][i - 1][1] in vb and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-2] == 'ㅎ' and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-3] == 'ㅑ':
                tmp = list(hgtk.text.decompose(sentenceInfo[0][i - 1])) 
                tmp[len(tmp)-3] = 'ㅒ'
                tmp[len(tmp)-2] = ''
                sentenceInfo[1][i - 1][0] = hgtk.text.compose(tmp)
                sentenceInfo[0][i - 1] = hgtk.text.compose(tmp)
                sentenceInfo[1][i][1] = ''
                sentenceInfo[1][i][0] = ''
                sentenceInfo[0][i] = ''
                break
        elif sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i][0] == '어' :
            if sentenceInfo[1][i - 1][1] in vb and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-2] == 'ㅎ':
                tmp = list(hgtk.text.decompose(sentenceInfo[0][i - 1])) 
                tmp[len(tmp)-3] = 'ㅔ'
                tmp[len(tmp)-2] = ''
                sentenceInfo[1][i - 1][0] = hgtk.text.compose(tmp)
                sentenceInfo[0][i - 1] = hgtk.text.compose(tmp)
                sentenceInfo[1][i][1] = ''
                sentenceInfo[1][i][0] = ''
                sentenceInfo[0][i] = ''
                break
        #ㅎ 불규칙 처리, 어미 '-아' 앞에서 ㅣ로 바뀌어 합쳐지는 활용 형식 / 해요체
        elif sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i][0] == '아요' :
            if sentenceInfo[1][i - 1][1] in vb and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-2] == 'ㅎ' and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-3] != 'ㅑ':
                tmp = list(hgtk.text.decompose(sentenceInfo[0][i - 1])) 
                tmp[len(tmp)-3] = 'ㅐ'
                tmp[len(tmp)-2] = ''
                sentenceInfo[1][i - 1][0] = hgtk.text.compose(tmp)
                sentenceInfo[0][i - 1] = hgtk.text.compose(tmp)
                sentenceInfo[1][i][0] = '요'
                sentenceInfo[0][i] = '요'
                break
            elif sentenceInfo[1][i - 1][1] in vb and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-2] == 'ㅎ' and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-3] == 'ㅑ':
                tmp = list(hgtk.text.decompose(sentenceInfo[0][i - 1])) 
                tmp[len(tmp)-3] = 'ㅒ'
                tmp[len(tmp)-2] = ''
                sentenceInfo[1][i - 1][0] = hgtk.text.compose(tmp)
                sentenceInfo[0][i - 1] = hgtk.text.compose(tmp)
                sentenceInfo[1][i][0] = '요'
                sentenceInfo[0][i] = '요'
                break
        elif sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i][0] == '어요' :
            if sentenceInfo[1][i - 1][1] in vb and hgtk.text.decompose(sentenceInfo[1][i - 1][0])[len(hgtk.text.decompose(sentenceInfo[1][i - 1][0]))-2] == 'ㅎ':
                tmp = list(hgtk.text.decompose(sentenceInfo[0][i - 1])) 
                tmp[len(tmp)-3] = 'ㅔ'
                tmp[len(tmp)-2] = ''
                sentenceInfo[1][i - 1][0] = hgtk.text.compose(tmp)
                sentenceInfo[0][i - 1] = hgtk.text.compose(tmp)
                sentenceInfo[1][i][0] = '요'
                sentenceInfo[0][i] = '요'
                break
    return sentenceInfo
        #으 불규칙 처리, 어미 '-아' 앞에서 사라지는 활용 형식
sentenceInfo = stemEndingIrregular(sentenceInfo)
print(sentenceInfo)
        

                    

            