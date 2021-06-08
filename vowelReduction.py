import hgtk

'''
    hgtkTest.py에 들어갈 Code.
    모음축약 : 1) 반모음 ㅣ 계열, 2) 반모음 ㅗ/ㅜ 계열
    시 처리 :  시+어 → 셔, 시+어요 → 세, 시+었 → 셨

    input : 문체변환처리가 끝난 komoran.morphs(), komoran.pos()
    output : 모음축약과 시처리를 한 komoran.morphs(), komoran.pos()
'''


def vowelReduction(sentenceInfo):
    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.decompose(sentenceInfo[1][i][0])

    for i in range(len(sentenceInfo[1])-1):
        # 반모임 ㅣ 계열 : ㅣ + 어 → ㅕ ex) 달리+어 = 달려
        if sentenceInfo[1][i][0] != 'ㅅㅣᴥ' and sentenceInfo[1][i][0] != 'ㅇㅡᴥㅅㅣᴥ' and sentenceInfo[1][i][0][-2:] == 'ㅣᴥ' and sentenceInfo[1][i+1][0][:3] == 'ㅇㅓᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅕ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅣ+ 었 → 였
        if sentenceInfo[1][i][0] != 'ㅅㅣᴥ' and sentenceInfo[1][i][0][-2:] == 'ㅣᴥ' and sentenceInfo[1][i+1][0][:4] == 'ㅇㅓㅆᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅕㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 반모임 ㅣ 계열 : ㅣ + ㅐ → ㅒ ex) ㅣ+애 = 얘
        if sentenceInfo[1][i][0][-2:] == 'ㅣᴥ' and sentenceInfo[1][i+1][0][:3] == 'ㅇㅐᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅒ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # 반모음 ㅗ/ㅜ 계열 :  ㅗ + ㅏ → ㅘ ex) 오+아서 = 와서
        if sentenceInfo[1][i][0][-2:] == 'ㅗᴥ' and sentenceInfo[1][i+1][0][:3] == 'ㅇㅏᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅘ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅗ + 았 → 왔
        if sentenceInfo[1][i][0][-2:] == 'ㅗᴥ' and sentenceInfo[1][i+1][0][:4] == 'ㅇㅏㅆᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅘㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 반모음 ㅗ/ㅜ 계열 : ㅜ + ㅓ → ㅝ ex) 두+어 = 둬
        if sentenceInfo[1][i][0][-2:] == 'ㅜᴥ' and sentenceInfo[1][i+1][0][:3] == 'ㅇㅓᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅝ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅜ + 었 → 웠
        if sentenceInfo[1][i][0][-2:] == 'ㅜᴥ' and sentenceInfo[1][i+1][0][:4] == 'ㅇㅓㅆᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅝㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 반모음 ㅗ/ㅜ 계열 : ㅚ + ㅓ → ㅙ ex) 되+어 = 돼
        if sentenceInfo[1][i][0][-2:] == 'ㅚᴥ' and sentenceInfo[1][i+1][0][:3] == 'ㅇㅓᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅙ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][3:]

        # ㅚ + 었 → 왰
        if sentenceInfo[1][i][0][-2:] == 'ㅚᴥ' and sentenceInfo[1][i+1][0][:4] == 'ㅇㅓㅆᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-2] + \
                'ㅙㅆ' + sentenceInfo[1][i][0][-1:]
            sentenceInfo[1][i+1][0] = sentenceInfo[1][i+1][0][4:]

        # 시+어요 → 셔요 ex) 레몬이 시다.
        if sentenceInfo[1][i][0] == 'ㅅㅣᴥ' and sentenceInfo[1][i][1] == 'VA' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥㅇㅛᴥ':
            sentenceInfo[1][i][0] = 'ㅅㅕᴥ'
            sentenceInfo[1][i+1][0] = '요ᴥ'
            sentenceInfo[1][i+1][1] = 'EF'

        # 시+어 → 셔
        if sentenceInfo[1][i][0] == 'ㅅㅣᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥ':
            sentenceInfo[1][i][0] = 'ㅅㅕᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

        # 시+어요 → 세요
        if sentenceInfo[1][i][0] == 'ㅅㅣᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥㅇㅛᴥ':
            sentenceInfo[1][i][0] = 'ㅅㅔᴥ'
            sentenceInfo[1][i+1][0] = 'ㅇㅛᴥ'

        # 시+었 → 셨
        if sentenceInfo[1][i][0] == 'ㅅㅣᴥ' and 'ㅇㅓㅆᴥ' in sentenceInfo[1][i+1][0]:
            sentenceInfo[1][i][0] = 'ㅅㅕㅆᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

        # 으시 + 어
        if len(sentenceInfo[1]) - 2 > i and sentenceInfo[1][i][0] == 'ㅇㅡᴥㅅㅣᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥ' and sentenceInfo[1][i+2][0] != 'ㅇㅛᴥ':
            sentenceInfo[1][i][0] = 'ㅇㅡᴥㅅㅕᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

        if len(sentenceInfo[1]) - 2 > i and sentenceInfo[1][i][0] == 'ㅇㅡᴥㅅㅣᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥ' and sentenceInfo[1][i+2][0] == 'ㅇㅛᴥ':
            sentenceInfo[1][i][0] = 'ㅇㅡᴥㅅㅔᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''
        # 으시 + 어요
        if sentenceInfo[1][i][0] == 'ㅇㅡᴥㅅㅣᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥㅇㅛᴥ':
            sentenceInfo[1][i][0] = 'ㅇㅡᴥㅅㅔᴥㅇㅛᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''
        # 으시 + 었
        if sentenceInfo[1][i][0] == 'ㅇㅡㅅㅣᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅓᴥ':
            sentenceInfo[1][i][0] = 'ㅇㅡᴥㅅㅕㅆᴥ'
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

        # 가았다 -> 갔다
        if sentenceInfo[1][i][0][-2:] == 'ㅏᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅏㅆᴥ':
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][0:-1] + 'ㅆᴥ'
            sentenceInfo[1][i+1][0] = ''

        # 가아 -> 가
        if sentenceInfo[1][i][0][-2:] == 'ㅏᴥ' and sentenceInfo[1][i+1][0] == 'ㅇㅏᴥ':
            sentenceInfo[1][i+1][0] = ''

        for i in range(len(sentenceInfo[0])):
            if len(sentenceInfo[1][i][0]) == 0:
                sentenceInfo[1][i][1] = ''

    # print(hgtkList)
    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.compose(sentenceInfo[1][i][0])

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo
