import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hgtk

inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence)
inputAnalyzer = naverPapago.translate(inputSentence)
morph_pos = komoranSpacing.Spacing(inputAnalyzer[1])

pos_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ'] # 양성 모음
neg_vowel = ['ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅢ'] # 음성 모음
consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'] # 자음
noun = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'XSN'] # 체언
vb = ['VV', 'VA', 'XSV', 'XSA'] # 용언

'''
input morph, pos 리스트와 문장종류
output morph, pos 리스트
'''
def haeyo_ver1(morph_pos, sentenceType):
    for i in range(len(morph_pos[1])):
        # 종결어미를 찾는다.
        if morph_pos[1][i][1] == 'EF' :
            # 전 형태소의 품사가 용언일 때
            if morph_pos[1][i - 1][1] in vb:
                # '하' 불규칙 처리를 위해 따로 빼놓음
                if morph_pos[1][i - 1][0] == '하':
                    morph_pos[0][i] = '아요'
                    morph_pos[1][i][0] = '아요'
                    continue
                tmp = morph_pos[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if verb[-1] in consonant:
                    # 전 형태소의 모음이 양성일 때
                    if verb[-2] in pos_vowel:
                        morph_pos[0][i] = '아요'
                        morph_pos[1][i][0] = '아요'
                    # 전 형태소의 모음이 음성일 때    
                    elif verb[-2] in neg_vowel:
                        morph_pos[0][i] = '어요'
                        morph_pos[1][i][0] = '어요'
                # 전 형태소의 받침이 없고 'ㅏ'나 'ㅓ'로 끝날 때
                elif verb[-2] == 'ㅏ' or verb[-2] == 'ㅓ':
                    morph_pos[0][i] = '요'
                    morph_pos[1][i][0] = '요'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in pos_vowel:
                    morph_pos[0][i] = '아요'
                    morph_pos[1][i][0] = '아요'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in neg_vowel:
                    morph_pos[0][i] = '어요'
                    morph_pos[1][i][0] = '어요'
            # 전 형태소가 '아니' 혹은 '이' 일 때
            elif morph_pos[1][i - 1][0] == '아니' or morph_pos[1][i - 1][0] == '이':
                morph_pos[0][i] = '에요'
                morph_pos[1][i][0] = '에요'
            # 전 형태소의 품사가 체언일 때
            elif morph_pos[1][i - 1][1] in noun:
                tmp = morph_pos[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if verb[-1] in consonant:
                    morph_pos[0][i] = '이에요'
                    morph_pos[1][i][0] = '이에요'
                # 전 형태소의 받침이 없을 때
                else:
                    morph_pos[0][i] = '예요'
                    morph_pos[1][i][0] = '예요'
    
    return morph_pos # morph, pos 리스트형으로 반환

haeyo_test = haeyo_ver1(morph_pos, sentenceType)
print(haeyo_test)

second_res = hgtkTest.textCompose(haeyo_test[0])
print(second_res)