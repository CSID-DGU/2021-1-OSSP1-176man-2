import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hae
import haera
import haeyo
import hapshow
import copy

# 사용자가 영어문장과 문체를 선택해서 입력
print("번역할 영어문장을 입력해주세요(문법적으로 완벽한 문장): ")
inputSentence = input()
print("번역된 문장의 문체를 선택해주세요(해, 해라, 해요, 합쇼): ")
inputSentenceStyle = input()

outputSentence = []

sentenceType = engInputAnalysis.sentenceType(inputSentence) # 문장종류 확인
sentenceInfo = naverPapago.translate(inputSentence) # 파파고API로 번역 및 Komoran으로 형태소 분석
tmp = komoranSpacing.Spacing(sentenceInfo[1]) # 분석된 형태소를 이용하여 띄어쓰기 처리
sentenceInfoList = []
for i in range(4):
    a = copy.deepcopy(tmp)
    sentenceInfoList.append(a)

# 사용자가 선택한 문체에 맞는 함수 실행후 어미 변경
sentenceHae = hae.hae(sentenceInfoList[0])
outputSentence.append(hgtkTest.textCompose(sentenceHae[0]))
sentenceHaera = haera.haera(sentenceInfoList[1], sentenceType)
outputSentence.append(hgtkTest.textCompose(sentenceHaera[0]))
sentenceHaeyo = haeyo.haeyo(sentenceInfoList[2], sentenceType)
outputSentence.append(hgtkTest.textCompose(sentenceHaeyo[0]))
sentenceHapshow = hapshow.hapshow(sentenceInfoList[3], sentenceType)
outputSentence.append(hgtkTest.textCompose(sentenceHapshow[0]))

print(outputSentence)