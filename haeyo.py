import hgtk

pos_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ'] # 양성 모음
neg_vowel = ['ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅢ'] # 음성 모음
noun = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'XSN'] # 체언
vb = ['VV', 'VA', 'VX', 'XSV', 'XSA'] # 용언

'''
input morph, pos 리스트와 문장종류
output morph, pos 리스트
'''
def haeyo(sentenceInfo, sentenceType):
    for i in range(len(sentenceInfo[1])):
        # 종결어미를 찾는다.
        if sentenceInfo[1][i][1] == 'EF' :
            # '하' 불규칙 처리를 위해 따로 빼놓음
            if sentenceInfo[1][i - 1][0] == '하':
                sentenceInfo[1][i][0] = '아요'
            # 전 형태소의 품사가 용언일 때
            elif sentenceInfo[1][i - 1][1] in vb:
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
            # 전 형태소가 '아니' 혹은 '이' 일 때
            elif sentenceInfo[1][i - 1][0] == '아니' or sentenceInfo[1][i - 1][0] == '이':
                sentenceInfo[1][i][0] = '에요'
            # 전 형태소의 품사가 체언일 때
            elif sentenceInfo[1][i - 1][1] in noun:
                tmp = sentenceInfo[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if hgtk.checker.has_batchim(verb[-1]):
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
    return sentenceInfo # morph, pos 리스트형으로 반환