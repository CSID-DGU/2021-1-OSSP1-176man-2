import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis

'''
    EP : 선어말어미, EF : 종결어미, EC : 연결 어미, ETN : 명사형 전성 어미, ETM : 관형형 전성어미
    VV : 동사, VA : 형용사, VCP : 긍정 지정사, VCN : 부정 지정사, VX : 보조 용언

    input : 번역된 문장에 대해 형태소 분석한 이중list [morphs, pos]와 번역된 문장의 종류
    output : 각 문장 종류에 따라 종결어미 변환한 이중list [morphs, pos]
    
    code 중간에 print는 원래는 지워야하는데 아직 예외처리 할 것도 있을거고 계속적인 수정을 할때 필요함으로 남겨둠.
    마지막에 완성시 지우겠음.
'''

inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence)
inputAnalyzer = naverPapago.translate(inputSentence)
Analyerlist = komoranSpacing.Spacing(inputAnalyzer[1])


def haera(Analyerlist, sentenceType):
    print(Analyerlist)  # 종결어미 처리 전
    print(sentenceType)  # 문장 종류

    if sentenceType == "statement":
        # ㄴ다/는다 : 종결어미 앞이 동사이면, 'ㅂ니다' → 'ㄴ다'로 수정
        for i in range(len(Analyerlist[1])):
            if Analyerlist[1][i] == ['ㅂ니다', 'EF'] and Analyerlist[1][i-1][1] in ['VV']:
                Analyerlist[0][i] = 'ㄴ다'
                Analyerlist[1][i] = ['ㄴ다', 'EF']

        # 다 : 종결어미 앞이 형용사, 서술격 조사일 경우, 'ㅂ니다' → '다'로 수정
        for i in range(len(Analyerlist[1])):
            if Analyerlist[1][i] == ['ㅂ니다', 'EF'] and Analyerlist[1][i-1][1] in ['VCP', 'VCN', 'VA']:
                Analyerlist[0][i] = '다'
                Analyerlist[1][i] = ['다', 'EF']

    elif sentenceType == "command":
        # 말아 → 마 : '말'을 '마'로 수정하고 '아' 삭제
        for i in range(len(Analyerlist[1])):
            if Analyerlist[1][i] == ['말', 'VX']:
                Analyerlist[0][i] = '마'
                Analyerlist[1][i] = ['마', 'VX']
                Analyerlist[0][i+1] = ''
                Analyerlist[1][i+1] = ['', '']

        # ex) 가라 → 가 : 종결어미 등장시 삭제
        for i in range(len(Analyerlist[1])):
            if Analyerlist[1][i][1] in ['EF']:
                Analyerlist[0][i] = ''
                Analyerlist[1][i] = ['', '']

    elif sentenceType == "question":
        # 종결어미 : '니', '나'
        for i in range(len(Analyerlist[1])):
            if Analyerlist[1][i][1] in ['EF']:
                Analyerlist[0][i] = '니'
                Analyerlist[1][i][0] = '니'  # '나'

    # 해 → 하아 : '하'를 '해'로 바꾸고 '아' 삭제
    for i in range(len(Analyerlist[1])-1):
        if Analyerlist[1][i] == ['하', 'VV'] and '아' in Analyerlist[1][i+1][0]:
            Analyerlist[1][i][0] = '해'
            Analyerlist[0][i] = '해'
            Analyerlist[1][i+1][0] = Analyerlist[1][i+1][0].replace('아', '')
            Analyerlist[0][i+1] = Analyerlist[0][i+1].replace('아', '')

    print(Analyerlist)  # 종결어미 처리 후

    CompleteString = hgtkTest.textCompose(Analyerlist[0])
    print(CompleteString)  # morphs → string : string으로 문장 출력.
    return Analyerlist


haera(Analyerlist, sentenceType)
