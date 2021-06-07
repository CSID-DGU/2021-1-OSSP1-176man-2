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
import josa

'''
@param inputSentence 사용자가 입력한 영어 문장
@param sentenceStyle 사용자가 선택한 문체 (해 : 0, 해라 : 1, 해요 : 2, 합쇼 : 3)
@param subjectHonorification 사용자가 선택한 주어 높임 여부 (높임 : 1, 안높임 : 0)
return outputSentence 사용자가 선택한 옵션에 해당하는 작업을 모두 수행한 번역 문장
'''


def main(inputSentence, inputSentenceStyle, subjectHonorification):
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
    sentenceInfo = komoranSpacing.Spacing(
        sentenceInfo[1])  # 분석된 형태소를 이용하여 띄어쓰기 처리
    # 주체 높임법 플래그, 불규칙 활용 여부 플래그 리스트에 추가
    sentenceInfo.append([subjectHonorification, 0])

    conversion.conversion(sentenceInfo, eng_pos)

    sentenceInfo = honorification.honorification1(
        sentenceInfo)  # 주체 높임에 따른 '시' 추가 및 삭제

    if inputSentenceStyle == 0:
        sentenceInfo = sentenceStyle.hae(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 1:
        sentenceInfo = sentenceStyle.haera(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 2:
        sentenceInfo = sentenceStyle.haeyo(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 3:
        sentenceInfo = sentenceStyle.habsyo(sentenceInfo, sentenceType)

    sentenceInfo = irregular.irregular(sentenceInfo)
    sentenceInfo = honorification.honorification2(sentenceInfo)

    if inputSentenceStyle == 0:
        sentenceInfo = sentenceStyle.hae(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 1:
        sentenceInfo = sentenceStyle.haera(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 2:
        sentenceInfo = sentenceStyle.haeyo(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 3:
        sentenceInfo = sentenceStyle.habsyo(sentenceInfo, sentenceType)

    sentenceInfo = josa.josa(sentenceInfo)
    sentenceInfo = vowelReduction.vowelReduction(sentenceInfo)
    outputSentence = hgtkTest.textCompose(sentenceInfo[0])

    print(outputSentence)
    return outputSentence


# # 사용자가 영어문장과 문체, 주어 높임을 선택해서 입력
# print("번역할 영어문장을 입력해주세요(문법적으로 완벽한 문장): ")
# inputSentence = input()
# print("번역된 문장의 문체를 선택해주세요(해, 해라, 해요, 합쇼): ")
# inputSentenceStyle = input()
# print("주어 높임 1, 주어 안높임 0: ")
# subjectHonorification = int(input())


# main(inputSentence, inputSentenceStyle, subjectHonorification)
