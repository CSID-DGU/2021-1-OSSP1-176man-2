import hgtk
'''
    EP : 선어말어미, EF : 종결어미, EC : 연결 어미, ETN : 명사형 전성 어미, ETM : 관형형 전성어미
    VV : 동사, VA : 형용사, VCP : 긍정 지정사, VCN : 부정 지정사, VX : 보조 용언

    input : 번역된 문장에 대해 형태소 분석한 이중list [morphs, pos]와 번역된 문장의 종류
    output : 각 문장 종류에 따라 종결어미 변환한 이중list [morphs, pos]
    
    code 중간에 print는 원래는 지워야하는데 아직 예외처리 할 것도 있을거고 계속적인 수정을 할때 필요함으로 남겨둠.
    마지막에 완성시 지우겠음.
'''


def haera(sentenceInfo, sentenceType):
    # print(sentenceInfo)  # 종결어미 처리 전
    # print(sentenceType)  # 문장 종류

    if sentenceType == "statement":

        # ㄴ다/는다 : 종결어미 앞이 동사이면, ㄴ다/는다로 변경
        for i in range(len(sentenceInfo[1])):
            if hgtk.checker.is_hangul(sentenceInfo[1][i-1][0][-1]):
                flag = hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][-1])
            else:
                flag = False

            if sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i-1][1] in ['VV'] and not flag:
                sentenceInfo[1][i] = ['ㄴ다', 'EF']

        for i in range(len(sentenceInfo[1])):
            if hgtk.checker.is_hangul(sentenceInfo[1][i-1][0][-1]):
                flag = hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][-1])
            else:
                flag = False

            if sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i-1][1] in ['VV'] and flag:
                sentenceInfo[1][i] = ['는다', 'EF']

        # 다 : 종결어미 앞이 서술격 조사일 경우
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i-1][1] in ['VCP', 'VCN']:
                sentenceInfo[1][i] = ['다', 'EF']

        # 군 : 종결어미 앞이 형용사인 경우, '군' → '다'로 수정
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] == 'EF' and sentenceInfo[1][i-1][1] == 'VA':
                sentenceInfo[1][i] = ['다', 'EF']

        # 어근 + 형용사 파생 접미사
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] == 'XSA' and sentenceInfo[1][i-1][1] == 'XR':
                sentenceInfo[1][i+1] = ['다', 'EF']

    elif sentenceType == "command":
        # 말아 → 마 : '말'을 '마'로 수정하고 '아' 삭제
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i] == ['말', 'VX']:
                sentenceInfo[1][i] = ['마', 'VX']
                sentenceInfo[1][i+1] = ['라', 'VX']

        # ex) 가라 → 가 : 종결어미 등장시 삭제
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] in ['EF'] and sentenceInfo[1][i][0] != "어라":
                sentenceInfo[1][i] = ['', '']

    elif sentenceType == "question":
        # 종결어미 : '니', '나'
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] in ['EF']:
                sentenceInfo[1][i][0] = '니'  # '나'

    # print(Analyzerlist)  # 종결어미 처리 후

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    # print(CompleteString)  # morphs → string : string으로 문장 출력
    return sentenceInfo


#sentenceInfo = [['그', '는', ' ', '선', '을', ' ', '긋', '는다', '.'], [['그', 'NP'], ['는', 'JX'], [' ', 'BLK'], ['선', 'NNG'], ['을', 'JKO'], [' ', 'BLK'], ['긋', 'VV'], ['는다', 'EF'], ['.', 'SF']]]
#print(haera(sentenceInfo, 'statement'))
