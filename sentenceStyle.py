import hgtk

pos_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅛ']
neg_vowel = ['ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅚ', 'ㅙ',
             'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅢ']
consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ',
             'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
noun = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'XSN']
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX', 'EP']

'''
2021-06-07 어미변환 함수 4개 merge
'''

# 어미 '해'체 변환 함수


def hae(sentenceInfo, sentenceType):
    for i in range(len(sentenceInfo[1])):
        # 종결어미를 찾는다.
        if sentenceInfo[1][i][1] == 'EF':
            # 전 형태소의 품사가 용언일 때
            if sentenceInfo[1][i - 1][1] in vb:
                # '하' 불규칙 처리를 위해 따로 빼놓음
                if sentenceInfo[1][i - 1][0] == '하':
                    sentenceInfo[1][i][0] = '아'
                    continue
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                if tmp[-1] == '르':
                    verb = hgtk.letter.decompose(tmp[-2])
                # 전 형태소의 받침이 있을 때
                if hgtk.checker.has_batchim(tmp[-1]):
                    '''
                    # 전 형태소의 모음이 양성일 때
                    if verb[-2] in pos_vowel:
                        sentenceInfo[1][i][0] = '아'
                    # 전 형태소의 모음이 음성일 때    
                    elif verb[-2] in neg_vowel:
                    '''
                    sentenceInfo[1][i][0] = '어'
                # 전 형태소의 받침이 없고 'ㅓ'로 끝날 때
                elif verb[-2] == 'ㅓ':
                    sentenceInfo[1][i][0] = '어'
                # 전 형태소의 받침이 없고 'ㅏ'로 끝날 때 ex)집에 가 에서 '가'
                elif verb[-2] == 'ㅏ':
                    sentenceInfo[1][i][0] = '아'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in pos_vowel:
                    sentenceInfo[1][i][0] = '아'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in neg_vowel:
                    sentenceInfo[1][i][0] = '어'
            # 전 형태소가 '아니' 혹은 '이' 일 때
            elif sentenceInfo[1][i - 1][0] == '아니' or sentenceInfo[1][i - 1][0] == '이':
                sentenceInfo[1][i][0] = '야'
            # 전 형태소의 품사가 체언일 때
            elif sentenceInfo[1][i - 1][1] in noun:
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if verb[-1] in consonant:
                    sentenceInfo[1][i][0] = '이야'
                # 전 형태소의 받침이 없을 때
                else:
                    sentenceInfo[1][i][0] = '야'

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    return sentenceInfo  # morph, pos 리스트형으로 반환

# 어미 '해라'체 변환 함수


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

            if isHangul and isBatchim and sentenceInfo[1][i][1] in ['VV', 'XSV', 'VX', 'XSA'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['는다', 'EF']
            if isHangul and not isBatchim and sentenceInfo[1][i][1] in ['VV', 'XSV', 'VX', 'XSA'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['ㄴ다', 'EF']

        # 다 : 종결어미 앞이 서술격 조사일 경우
        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] in ['VCP', 'VCN', 'NNB', 'EP', 'VX'] and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['다', 'EF']

        for i in range(len(sentenceInfo[1])):
            if sentenceInfo[1][i][1] in vb and sentenceInfo[1][i+1] == ['시', 'EP'] and sentenceInfo[1][i+2][1] == 'EF':
                sentenceInfo[1][i+2] = ['ㄴ다', 'EF']

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

            if isHangul and isBatchim and sentenceInfo[1][i][1] in vb and sentenceInfo[1][i+1][1] == 'EF':
                sentenceInfo[1][i+1] = ['어라', 'EF']
            if isHangul and not isBatchim and sentenceInfo[1][i][1] in vb and sentenceInfo[1][i+1][1] == 'EF':
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

# 어미 '해요'체 변환 함수


def haeyo(sentenceInfo, sentenceType):
    for i in range(len(sentenceInfo[1])):
        # 종결어미를 찾는다.
        if sentenceInfo[1][i][1] == 'EF':
            # '하' 불규칙 처리를 위해 따로 빼놓음
            flag_ha = sentenceInfo[1][i - 1][0]
            if flag_ha[-1] == '하':
                sentenceInfo[1][i][0] = '아요'
            # 전 형태소의 품사가 용언일 때
            elif sentenceInfo[1][i - 1][1] in vb:
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                if tmp[-1] == '르':
                    verb = hgtk.letter.decompose(tmp[-2])
                # 전 형태소의 받침이 있을 때
                if hgtk.checker.has_batchim(tmp[-1]):
                    sentenceInfo[1][i][0] = '어요'
                # 전 형태소의 받침이 없고 'ㅏ'나 'ㅓ'로 끝날 때
                elif verb[-2] == 'ㅏ' or verb[-2] == 'ㅓ':
                    sentenceInfo[1][i][0] = '요'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in pos_vowel:
                    sentenceInfo[1][i][0] = '아요'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in neg_vowel:
                    sentenceInfo[1][i][0] = '어요'
            # 전 형태소가 '아니' 혹은 '이' 일 때
            elif sentenceInfo[1][i - 1][0] == '아니' or sentenceInfo[1][i - 1][0] == '이':
                sentenceInfo[1][i][0] = '에요'
            # 전 형태소의 품사가 체언일 때
            elif sentenceInfo[1][i - 1][1] in noun:
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if hgtk.checker.has_batchim(tmp[-1]):
                    sentenceInfo[1][i][0] = '이에요'
                # 전 형태소의 받침이 없을 때
                else:
                    sentenceInfo[1][i][0] = '예요'
            # 전 형태소의 품사가 용언이나, 체언이 아닐 때
            else:
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if hgtk.checker.has_batchim(tmp[-1]):
                    # 전 형태소의 모음이 양성일 때
                    if verb[-2] in pos_vowel:
                        sentenceInfo[1][i][0] = '아요'
                    # 전 형태소의 모음이 음성일 때
                    elif verb[-2] in neg_vowel:
                        sentenceInfo[1][i][0] = '어요'
                # 전 형태소의 받침이 없고 'ㅏ'나 'ㅓ'로 끝날 때
                elif verb[-2] == 'ㅏ' or verb[-2] == 'ㅓ':
                    sentenceInfo[1][i][0] = '요'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in pos_vowel:
                    sentenceInfo[1][i][0] = '아요'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in neg_vowel:
                    sentenceInfo[1][i][0] = '어요'

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    return sentenceInfo  # morph, pos 리스트형으로 반환

# 어미 '합쇼'체 변환 함수


def habsyo(sentenceInfo, sentenceType):
    # word_class : 어미 변경시 변경되어야 할 품사(종결어미)를 저장한 배열
    word_class = ["EF"]

    # tuple의 값이 변경가능하도록 list 형식으로 변경
    sentenceInfo[1] = list(map(list, sentenceInfo[1]))

    # 평서문인 경우
    if sentenceType == "statement":
        for i in range(len(sentenceInfo[1])):
            # 종결 어미를 찾은 경우
            if sentenceInfo[1][i][1] in word_class:
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]):
                    sentenceInfo[1][i][0] = "습니다"
                # 앞 음절이 받침이 없는 경우
                else:
                    sentenceInfo[1][i][0] = "ㅂ니다"

    # 의문문인 경우
    elif sentenceType == "question":
        for i in range(len(sentenceInfo[1])):
            # 종결 어미를 찾은 경우
            if sentenceInfo[1][i][1] in word_class:
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]):
                    sentenceInfo[1][i][0] = "습니까"
                # 앞 음절이 받침이 없는 경우
                else:
                    sentenceInfo[1][i][0] = "ㅂ니까"

    # 명령형인 경우
    elif sentenceType == "command":
        for i in range(len(sentenceInfo[1])):
            # 종결 어미를 찾은 경우
            if sentenceInfo[1][i][1] in word_class:
                sentenceInfo[1][i][0] = "ㅂ시오"

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo
