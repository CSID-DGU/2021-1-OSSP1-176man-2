import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import sentenceStyle
import irregular
import honorification
import conversion
import vowelReduction
import josa
import config
import pandas as pd
import random

FILE_PATH = config.FILE_PATH  # 말뭉치 excel 파일이 위치한 경로


def getCorpus(fname, start_idx=40, idx_range=20):
    excelTitle = FILE_PATH + fname  # 경로 + 파일명
    excel_dafaframe = pd.read_excel(
        excelTitle + ".xlsx", engine='openpyxl')  # 원본 excel 파일
    eng_list = list((excel_dafaframe['번역문']))  # 영어 문장 (번역문)
    kor_list = list((excel_dafaframe['원문']))  # 한국어 문장 (원문)

    si = start_idx
    cnt = 0
    while True:
        # 리스트에서 원하는 range의 문장들이 찾아졌을 때, 리스트의 범위를 초과하였을 때
        if cnt > idx_range or si >= len(eng_list):
            break

        # 영어 문장이 250자를 초과할 때 리스트에서 제외
        if len(eng_list[si]) > 250:
            eng_list.pop(si)
            kor_list.pop(si)
        else:
            cnt += 1
            si += 1

        result = list(
            map(lambda x, y: [x, y], eng_list[start_idx: start_idx + idx_range], kor_list[start_idx: start_idx + idx_range]))

        return result
        # return [eng_list[start_idx: start_idx + idx_range], kor_list[start_idx: start_idx + idx_range]]


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
    print(sentenceInfo, end="1\n")
    conversion.conversion(sentenceInfo, eng_pos)

    sentenceInfo = honorification.honorification1(
        sentenceInfo)  # 주체 높임에 따른 '시' 추가 및 삭제
    print(sentenceInfo, end="2\n")
    if inputSentenceStyle == 0:
        sentenceInfo = sentenceStyle.hae(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 1:
        sentenceInfo = sentenceStyle.haera(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 2:
        sentenceInfo = sentenceStyle.haeyo(sentenceInfo, sentenceType)
    elif inputSentenceStyle == 3:
        sentenceInfo = sentenceStyle.habsyo(sentenceInfo, sentenceType)
    print(sentenceInfo, end="3\n")
    if sentenceInfo[2][1] == 1:
        sentenceInfo = irregular.irregular(sentenceInfo)
    print(sentenceInfo, end="4\n")
    sentenceInfo = honorification.honorification2(sentenceInfo)
    print(sentenceInfo, end="5\n")
    sentenceInfo = josa.josa(sentenceInfo)
    print(sentenceInfo, end="6\n")
    sentenceInfo = vowelReduction.vowelReduction(sentenceInfo)
    print(sentenceInfo, end="7\n")
    outputSentence = hgtkTest.textCompose(sentenceInfo[0])

    print(sentenceType)
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

def testing():
    testList = getCorpus("test")

    for idx, test in enumerate(testList):
        print("Test Num.", idx)
        print(test[1])
        input()
        for i in range(4):

            main(test[0], i, 0)
            print("------")
            print(test[0])
            print(test[1])
            flag = input("")
            if flag == '-1':
                break
            main(test[0], i, 1)
            print("------")
            print(test[0])
            print(test[1])
            flag = input("")
            if flag == '-1':
                break


testing()
# print(random.sample(range(0, 100298), 20))
