import hgtk


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
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + \
                sentenceInfo[1][i+1][0][0] + "ᴥ"
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][0] = ''

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
        if 'ㄹᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i+1][0][0] in ['ㄴ', 'ㄹ', 'ㅂ'] and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"
        if 'ㄹᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i+1][0][0:2] in ['ㅇㅗ', 'ㅅㅣ'] and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"

    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.compose(sentenceInfo[1][i][0])

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo


# sentenceInfo = [['너', '가', ' ', '기쁘', '어서', ' ', '나', '도', ' ', '행복', '해', '', '.'], [['너', 'NP'], ['가', 'JKS'], [' ', 'BLK'], [
    '기쁘', 'VA'], ['어서', 'EC'], [' ', 'BLK'], ['나', 'NP'], ['도', 'JX'], [' ', 'BLK'], ['행복', 'NNG'], ['해', 'XSV'], ['', ''], ['.', 'SF']]]
# print(irregular_all(sentenceInfo))

# sentenceInfo = [['너', '가', ' ', '살', '는', ' ', '집', '에', ' ', '나', '도', ' ', '갈래', '.'], [['너', 'NP'], ['가', 'JKS'], [' ', 'BLK'], ['살', 'VV'], [
    '는', 'ETM'], [' ', 'BLK'], ['집', 'NNG'], ['에', 'JKB'], [' ', 'BLK'], ['나', 'NP'], ['도', 'JX'], [' ', 'BLK'], ['갈래', 'NNG'], ['.', 'SF']]]
# print(irregular_all(sentenceInfo))

# sentenceInfo = [['그', '의', ' ', '얼굴', '은', ' ', '빨갛', '어', '.'], [['그', 'NP'], ['의', 'JKG'], [
    ' ', 'BLK'], ['얼굴', 'NNG'], ['은', 'JX'], [' ', 'BLK'], ['빨갛', 'VA'], ['어', 'EF'], ['.', 'SF']]]
# print(irregular_all(sentenceInfo))

# sentenceInfo = [['내', ' ', '빨갛', 'ㄴ', ' ', '얼굴', '은', ' ', '멋지', '어', '.'], [['내', 'NP'], [' ', 'BLK'], ['빨갛', 'VA'], [
    'ㄴ', 'ETM'], [' ', 'BLK'], ['얼굴', 'NNG'], ['은', 'JX'], [' ', 'BLK'], ['멋지', 'VA'], ['어', 'EF'], ['.', 'SF']]]
# print(irregular_all(sentenceInfo))
