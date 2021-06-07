import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import sentenceStyle
import copy
import irregular
import honorification
import conversion
import vowelReduction

'''
@param inputSentence 사용자가 입력한 영어 문장
@param sentenceStyle 사용자가 선택한 문체 (해 : 0, 해라 : 1, 해요 : 2, 합쇼 : 3)
@param subjectHonorification 사용자가 선택한 주어 높임 여부 (높임 : 1, 안높임 : 0)
return outputSentence 사용자가 선택한 옵션에 해당하는 작업을 모두 수행한 번역 문장
'''


def main(inputSentence, inputSentenceStyle, subjectHonorification):
    outputSentence = []
    inputSentenceStyle, subjectHonorification = int(
        inputSentenceStyle), int(subjectHonorification)

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

    sentenceInfo, eng_pos = naverPapago.translate(
        inputSentence)  # 파파고API로 번역 및 Komoran으로 형태소 분석
    tmp = komoranSpacing.Spacing(sentenceInfo[1])  # 분석된 형태소를 이용하여 띄어쓰기 처리
    tmp.append([subjectHonorification, 0])  # 주체 높임법 플래그, 불규칙 활용 여부 플래그 리스트에 추가

    print(eng_pos)
    print(tmp)
    conversion.conversion(tmp, eng_pos)

    tmp = honorification.honorification1(tmp)  # 주체 높임에 따른 '시' 추가 및 삭제
    sentenceInfoList = []
    for i in range(4):
        a = copy.deepcopy(tmp)
        sentenceInfoList.append(a)

    print(tmp)

    # 각 문체에 맞는 함수 실행후 어미 변경, 불규칙 처리 확인
    # 해
    sentenceHae = sentenceStyle.hae(sentenceInfoList[0], sentenceType)
    sentenceHae = irregular.irregular(sentenceHae)
    sentenceHae = honorification.honorification2(sentenceHae)
    sentenceHae = vowelReduction.vowelReduction(sentenceHae)
    outputSentence.append(hgtkTest.textCompose(sentenceHae[0]))
    # 해라
    sentenceHaera = sentenceStyle.haera(sentenceInfoList[1], sentenceType)
    sentenceHaera = irregular.irregular(sentenceHaera)
    sentenceHaera = honorification.honorification2(sentenceHaera)
    sentenceHaera = vowelReduction.vowelReduction(sentenceHaera)
    outputSentence.append(hgtkTest.textCompose(sentenceHaera[0]))
    # 해요
    sentenceHaeyo = sentenceStyle.haeyo(sentenceInfoList[2], sentenceType)
    sentenceHaeyo = irregular.irregular(sentenceHaeyo)
    sentenceHaeyo = honorification.honorification2(sentenceHaeyo)
    sentenceHaeyo = vowelReduction.vowelReduction(sentenceHaeyo)
    outputSentence.append(hgtkTest.textCompose(sentenceHaeyo[0]))
    # 합쇼
    sentenceHabsyo = sentenceStyle.habsyo(sentenceInfoList[3], sentenceType)
    sentenceHabsyo = irregular.irregular(sentenceHabsyo)
    sentenceHabsyo = honorification.honorification2(sentenceHabsyo)
    sentenceHabsyo = vowelReduction.vowelReduction(sentenceHabsyo)
    outputSentence.append(hgtkTest.textCompose(sentenceHabsyo[0]))

    print(outputSentence)
    return outputSentence[inputSentenceStyle]


# # 사용자가 영어문장과 문체, 주어 높임을 선택해서 입력
# print("번역할 영어문장을 입력해주세요(문법적으로 완벽한 문장): ")
# inputSentence = input()
# print("번역된 문장의 문체를 선택해주세요(해, 해라, 해요, 합쇼): ")
# inputSentenceStyle = input()
# print("주어 높임 1, 주어 안높임 0: ")
# subjectHonorification = int(input())


# main(inputSentence, inputSentenceStyle, subjectHonorification)
