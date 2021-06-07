import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import sentenceStyle
import copy
import irregular
import honorification
import conversion

# 사용자가 영어문장과 문체, 주어 높임을 선택해서 입력
print("번역할 영어문장을 입력해주세요(문법적으로 완벽한 문장): ")
inputSentence = input()
print("번역된 문장의 문체를 선택해주세요(해, 해라, 해요, 합쇼): ")
inputSentenceStyle = input()
print("주어 높임 1, 주어 안높임 0: ")
subjectHonorification = int(input())

outputSentence = []

sentenceType = engInputAnalysis.sentenceType(inputSentence)  # 문장종류 확인
# 주체 높임법 예외처리
if sentenceType == 'command':
    if subjectHonorification == 1:
        if inputSentenceStyle == '해' or inputSentenceStyle == '해라':
            print("error")
            exit(1)
    elif subjectHonorification == 0:
        if inputSentenceStyle == '해요' or inputSentenceStyle == '합쇼':
            print("error")
            exit(1)

sentenceInfo, eng_pos = naverPapago.translate(inputSentence)  # 파파고API로 번역 및 Komoran으로 형태소 분석
tmp = komoranSpacing.Spacing(sentenceInfo[1])  # 분석된 형태소를 이용하여 띄어쓰기 처리
tmp.append([subjectHonorification, 0])  # 주체 높임법 플래그, 불규칙 활용 여부 플래그 리스트에 추가

print(eng_pos)
conversion.conversion(tmp, eng_pos)

print(tmp)

tmp = honorification.honorification(tmp)  # 주체 높임에 따른 '시' 추가 및 삭제
sentenceInfoList = []
for i in range(4):
    a = copy.deepcopy(tmp)
    sentenceInfoList.append(a)

print(tmp)

# 각 문체에 맞는 함수 실행후 어미 변경, 불규칙 처리 확인
sentenceHae = sentenceStyle.hae(sentenceInfoList[0], sentenceType)
sentenceHae = irregular.irregular(sentenceHae)
outputSentence.append(hgtkTest.textCompose(sentenceHae[0]))
sentenceHaera = sentenceStyle.haera(sentenceInfoList[0], sentenceType)
sentenceHaera = irregular.irregular(sentenceHaera)
outputSentence.append(hgtkTest.textCompose(sentenceHaera[0]))
sentenceHaeyo = sentenceStyle.haeyo(sentenceInfoList[0], sentenceType)
sentenceHaeyo = irregular.irregular(sentenceHaeyo)
outputSentence.append(hgtkTest.textCompose(sentenceHaeyo[0]))
sentenceHabsyo = sentenceStyle.habsyo(sentenceInfoList[0], sentenceType)
sentenceHabsyo = irregular.irregular(sentenceHabsyo)
outputSentence.append(hgtkTest.textCompose(sentenceHabsyo[0]))

print(outputSentence)
