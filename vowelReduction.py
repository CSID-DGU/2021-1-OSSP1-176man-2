import hgtk

'''
    hgtkTest.py에 들어갈 Code.
    모음축약 : 1) 반모음 ㅣ 계열, 2) 반모음 ㅗ/ㅜ 계열
    시 처리 :  시+어 → 세, 시+었 → 셨
    
    input : 문체변환처리가 끝난 komoran.morphs()
    output : 모음축약과 시처리를 한 komoran.morhs() 
'''


def vowelReduction(morphs):

    hgtkList = []
    for m in morphs:
        hgtkList.append(hgtk.text.decompose(m))

    for i in range(len(hgtkList)):
        # 반모임 ㅣ 계열 : ㅣ + 어 → ㅕ ex) 달리+어 = 달려
        if 'ㅅㅣᴥ' not in hgtkList[i] and 'ㅣᴥ' in hgtkList[i] and 'ㅇㅓᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅕ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][3:]

        # ㅣ+ 었 → 였
        if 'ㅅㅣᴥ' not in hgtkList[i] and 'ㅣᴥ' in hgtkList[i] and 'ㅇㅓㅆᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅕㅆ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][4:]

        # 반모임 ㅣ 계열 : ㅣ + ㅐ → ㅒ ex) ㅣ+애 = 얘
        if 'ㅣᴥ' in hgtkList[i] and 'ㅇㅐᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅒ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][3:]

        # 반모음 ㅗ/ㅜ 계열 :  ㅗ + ㅏ → ㅘ ex) 오+아서 = 와서
        if 'ㅗᴥ' in hgtkList[i] and 'ㅇㅏᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅘ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][3:]

        # ㅗ + 았 → 왔
        if 'ㅗᴥ' in hgtkList[i] and 'ㅇㅏㅆᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅘㅆ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][4:]

        # 반모음 ㅗ/ㅜ 계열 : ㅜ + ㅓ → ㅝ ex) 두+어 = 둬
        if 'ㅜᴥ' in hgtkList[i] and 'ㅇㅓᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅝ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][3:]

        # ㅜ + 었 → 웠
        if 'ㅜᴥ' in hgtkList[i] and 'ㅇㅓㅆᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅝㅆ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][4:]

        # 반모음 ㅗ/ㅜ 계열 : ㅚ + ㅓ → ㅙ ex) 되+어 = 돼
        if 'ㅚᴥ' in hgtkList[i] and 'ㅇㅓᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅙ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][3:]

        # ㅚ + 었 → 왰
        if 'ㅚᴥ' in hgtkList[i] and 'ㅇㅓㅆᴥ' in hgtkList[i+1]:
            hgtkList[i] = hgtkList[i][0:-2] + 'ㅙㅆ' + hgtkList[i][-1:]
            hgtkList[i+1] = hgtkList[i+1][4:]

        # 시+어 → 세
        if 'ㅅㅣᴥ' in hgtkList[i] and 'ㅇㅓᴥ' in hgtkList[i+1]:
            hgtkList[i] = 'ㅅㅔᴥ'
            hgtkList[i+1] = 'ㅇㅛᴥ'

        # 시+었 → 셨
        if 'ㅅㅣᴥ' in hgtkList[i] and 'ㅇㅓㅆᴥ' in hgtkList[i+1]:
            hgtkList[i] = 'ㅅㅕㅆᴥ'
            hgtkList[i+1] = 'ᴥ'

    # print(hgtkList)
    morphs = []
    for i in hgtkList:
        morphs.append(hgtk.text.compose(i))

    return morphs