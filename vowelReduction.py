import hgtk

'''
    hgtkTest.py에 들어갈 Code.
    모음축약 : 1) 반모음 ㅣ 계열, 2) 반모음 ㅗ/ㅜ 계열
    시 처리 :  시+어 → 세, 시+었 → 셨
    
    input : 문체변환처리가 끝난 komoran.morphs()
    output : 모음축약과 시처리를 한 komoran.morhs() 
'''


def vowelReduction(sentenceInfo):

    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.decompose(sentenceInfo[1][i][0])

    for i in range(len(sentenceInfo[1])):
        # 반모임 ㅣ 계열 : ㅣ + 어 → ㅕ ex) 달리+어 = 달려
        if 'ㅅㅣᴥ' not in sentenceInfo[1][i][0] and 'ㅣᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅕ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅣ+ 었 → 였
        if 'ㅅㅣᴥ' not in sentenceInfo[1][i][0] and 'ㅣᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓㅆᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅕㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 반모임 ㅣ 계열 : ㅣ + ㅐ → ㅒ ex) ㅣ+애 = 얘
        if 'ㅣᴥ' in sentenceInfo[1][i][0] and 'ㅇㅐᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅒ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # 반모음 ㅗ/ㅜ 계열 :  ㅗ + ㅏ → ㅘ ex) 오+아서 = 와서
        if 'ㅗᴥ' in sentenceInfo[1][i][0] and 'ㅇㅏᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅘ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅗ + 았 → 왔
        if 'ㅗᴥ' in sentenceInfo[1][i][0] and 'ㅇㅏㅆᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅘㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 반모음 ㅗ/ㅜ 계열 : ㅜ + ㅓ → ㅝ ex) 두+어 = 둬
        if 'ㅜᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅝ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅜ + 었 → 웠
        if 'ㅜᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓㅆᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅝㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 반모음 ㅗ/ㅜ 계열 : ㅚ + ㅓ → ㅙ ex) 되+어 = 돼
        if 'ㅚᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅙ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅚ + 었 → 왰
        if 'ㅚᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓㅆᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅙㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 시+어 → 셔
        if 'ㅅㅣᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥ':
            sentenceInfo[1][i][0] = 'ㅅㅕᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

        # 시+어요 → 세요
        if 'ㅅㅣᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥㅇㅛ':
            sentenceInfo[1][i][0] = 'ㅅㅔᴥ'
            sentenceInfo[1][i+1][0] = 'ㅇㅛᴥ'

        # 시+었 → 셨
        if 'ㅅㅣᴥ' in sentenceInfo[1][i][0] and 'ㅇㅓㅆᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = 'ㅅㅕㅆᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

        for i in range(len(sentenceInfo[0])):
            if len(sentenceInfo[1][i][0]) == 0:
                sentenceInfo[1][i][1] = ''

    # print(hgtkList)
    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.compose(sentenceInfo[1][i][0])

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo


#sentenceInfo = [['내', ' ', '남동생', '이', ' ', '학교', '에', ' ', '오', '았', '다', '.'], [['내', 'NP'], [' ', 'BLK'], ['남동생', 'NNP'], ['이', 'JKS'], [' ', 'BLK'], ['학교', 'NNG'], ['에', 'JKB'], [' ', 'BLK'], ['오', 'VX'], ['았', 'EP'], ['다', 'EF'], ['.', 'SF']]]
# print(vowelReduction(sentenceInfo))
