import hgtk

pos_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ']
neg_vowel = ['ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅢ']
consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
noun = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'XSN'] 
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX', 'EP']

def hae(sentenceInfo, sentenceType):
    for i in range(len(sentenceInfo[1])):         
        # 종결어미를 찾는다.
        if sentenceInfo[1][i][1] == 'EF' :
            # 전 형태소의 품사가 용언일 때
            if sentenceInfo[1][i - 1][1] in vb:
                # '하' 불규칙 처리를 위해 따로 빼놓음
                if sentenceInfo[1][i - 1][0] == '하':
                    sentenceInfo[1][i][0] = '아'
                    continue
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if verb[-1] in consonant:
                    # 전 형태소의 모음이 양성일 때
                    if verb[-2] in pos_vowel:
                        sentenceInfo[1][i][0] = '아'
                    # 전 형태소의 모음이 음성일 때    
                    elif verb[-2] in neg_vowel:
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
    return sentenceInfo # morph, pos 리스트형으로 반환