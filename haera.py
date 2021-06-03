import hgtk
#import naverPapago
#import komoranSpacing
#import hgtkTest
#import engInputAnalysis

'''
    EP : 선어말어미, EF : 종결어미, EC : 연결 어미, ETN : 명사형 전성 어미, ETM : 관형형 전성어미
    VV : 동사, VA : 형용사, VCP : 긍정 지정사, VCN : 부정 지정사, VX : 보조 용언

    input : 번역된 문장에 대해 형태소 분석한 이중list [morphs, pos]와 번역된 문장의 종류
    output : 각 문장 종류에 따라 종결어미 변환한 이중list [morphs, pos]
    
    code 중간에 print는 원래는 지워야하는데 아직 예외처리 할 것도 있을거고 계속적인 수정을 할때 필요함으로 남겨둠.
    마지막에 완성시 지우겠음.
'''
#inputSentence = input()
#sentenceType = engInputAnalysis.sentenceType(inputSentence)
#inputAnalyzer = naverPapago.translate(inputSentence)
#Analyzerlist1 = komoranSpacing.Spacing(inputAnalyzer[1])

# print(Analyzerlist1)


def haera(sentenceInfo, sentenceType):
    # print(sentenceInfo)  # 종결어미 처리 전
    # print(sentenceType)  # 문장 종류
    # print(sentenceType)
    if sentenceType == "statement":
        # ㄴ다/는다 : 종결어미 앞이 동사이면, ㄴ다/는다로 변경, 동사마지막의 받침여부로 나눔.
        for i in range(len(sentenceInfo[1])):
            isHangul = False
            isBatchim = False
            if hgtk.checker.is_hangul(sentenceInfo[1][i][0][-1]):
                isHangul = True
                if hgtk.checker.has_batchim(sentenceInfo[1][i][0][-1]):
                    isBatchim = True
            else:
                isHangul = False

            if isHangul and isBatchim and sentenceInfo[1][i][1] in ['VV', 'XSV'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['는다', 'EF']
            if isHangul and not isBatchim and sentenceInfo[1][i][1] in ['VV', 'XSV'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['ㄴ다', 'EF']

        # 다 : 종결어미 앞이 서술격 조사일 경우
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] in ['VCP', 'VCN', 'VX', 'NNB', 'EP'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['다', 'EF']

        # 종결어미 앞이 형용사인 경우, '군' → '다'로 수정
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] == 'VA' and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['다', 'EF']

        # 형용사 + '었' EP, + EF → EF를 '다'로 수정
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] == 'VA' and sentenceInfo[1][i+1][1] == 'EP':
                if sentenceInfo[1][i+2][1] == 'EF':
                    sentenceInfo[1][i+2] = ['다', 'EF']

        # 어근 + 형용사 파생 접미사
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] == 'XR' and sentenceInfo[1][i+1][1] == 'XSA' and sentenceInfo[1][i+1][0] != '하':
                sentenceInfo[1][i+1] = ['다', 'EF']
            if sentenceInfo[1][i][1] == 'XR' and sentenceInfo[1][i+1] == ['하', 'XSA'] and sentenceInfo[1][i+2][1] == 'EF':
                sentenceInfo[1][i+2] = ['다', 'EF']
    elif sentenceType == "command":
        exception = list(map(lambda x: x[1], sentenceInfo[1]))
        # 말아 → 마 : '말'을 '마'로 수정하고 '아' 삭제
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i] == ['말', 'VX']:
                sentenceInfo[1][i] = ['마', 'VX']
                sentenceInfo[1][i+1] = ['라', 'VX']

        # ex) 가라 → 가 : 종결어미 등장시 삭제
        for i in range(len(sentenceInfo[1])):
            isHangul = False
            isBatchim = False
            if hgtk.checker.is_hangul(sentenceInfo[1][i][0][-1]):
                isHangul = True
                if hgtk.checker.has_batchim(sentenceInfo[1][i][0][-1]):
                    isBatchim = True
            else:
                isHangul = False

            if isHangul and isBatchim and sentenceInfo[1][i][1] in ['VV'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['어라', 'EF']
            if isHangul and not isBatchim and sentenceInfo[1][i][1] in ['VV'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['라', 'EF']

        if 'EF' not in exception:
            sentenceInfo[1].insert(-1, ['라', 'EF'])

    elif sentenceType == "question":
        # 종결어미 : '니', '나'
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] in ['EF']:
                sentenceInfo[1][i][0] = '니'  # '나'

    # print(Analyzerlist)  # 종결어미 처리 후

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    # print(CompleteString)  # morphs → string : string으로 문장 출력
    return sentenceInfo


#print(haera(Analyzerlist1, sentenceType))
