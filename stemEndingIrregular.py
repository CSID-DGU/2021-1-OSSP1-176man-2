import hgtk
'''
import naverPapago
import komoranSpacing
import hae
import engInputAnalysis
'''

#수정 필요 사항
'''
좋아 -> 제로 바뀌는 것 수정 필요

'''

#testing code
'''
inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence) # 문장종류 확인
sentenceInfo = naverPapago.translate(inputSentence) # 파파고API로 번역 및 Komoran으로 형태소 분석
sentenceInfo = komoranSpacing.Spacing(sentenceInfo[1])
#print(sentenceInfo[1])
sentenceInfo = hae.hae(sentenceInfo,'Command')
'''
def stemEndingIrregular(sentenceInfo):
    
    stem = ['VV', 'VA', 'VX', 'VCP', 'VCN']
    ending = ['EP', 'EF', 'EC', 'ETN', 'ETM']

    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.decompose(sentenceInfo[1][i][0])

    # ㅎ 불규칙 활용
    for i in range(len(sentenceInfo[1])):
        if sentenceInfo[1][i][0][-2:] == 'ㅎᴥ' and sentenceInfo[1][i][1] in ['VA'] and sentenceInfo[1][i+1][0][1] == 'ㅓ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-3] + "ㅐᴥ"
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''
        if sentenceInfo[1][i][0][-2:] == 'ㅎᴥ' and sentenceInfo[1][i][1] in ['VA'] and sentenceInfo[1][i+1][0][1] == 'ㅏ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-3] + "ㅔᴥ"
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

    for i in range(len(sentenceInfo[1])):
        if sentenceInfo[1][i][0][-2:] == 'ㅎᴥ' and sentenceInfo[1][i][1] in ['VA'] and (sentenceInfo[1][i+1][0][0] == 'ㄴ' or sentenceInfo[1][i+1][0][0] == 'ㅁ'):
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"

    # 으 규칙 활용
    for i in range(len(sentenceInfo[1])):
        if 'ㅡᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i][1] in stem and sentenceInfo[1][i+1][0][0:2] == 'ㅇㅓ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][: -2] + \
                sentenceInfo[1][i+1][0][1:]
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

    for i in range(len(sentenceInfo[1])):
        if 'ㅡᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i][1] in stem and sentenceInfo[1][i+1][0][0:2] == 'ㅇㅏ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][: -2] + \
                sentenceInfo[1][i+1][0][1:]
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

    # ㄹ 규칙 활용
    for i in range(len(sentenceInfo[1])):
        if sentenceInfo[1][i][0] in ['.', '!', '?']:
            break
        if len(sentenceInfo[1][i+1][0]) == 0:
            continue
        if sentenceInfo[1][i][0][-2:] == 'ㄹᴥ' and sentenceInfo[1][i+1][0][0] in ['ㄴ', 'ㄹ', 'ㅂ'] and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"
        if sentenceInfo[1][i][0][-2:] == 'ㄹᴥ' and sentenceInfo[1][i+1][0][0:2] in ['ㅇㅗ', 'ㅅㅣ'] and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"

    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.compose(sentenceInfo[1][i][0])

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo

#testing code
'''
sentenceInfo = stemEndingIrregular(sentenceInfo)
print(sentenceInfo[1])
print(hgtk.text.compose(sentenceInfo[0]))
'''