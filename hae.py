import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hgtk
'''
    기존의 hae는 오류가 많고 예외처리가 되어있지 않은 것도 많음
    '해요' 체에서 '해'체에 필요한 요소를 추가하고 수정
    
'''


pos_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ']
neg_vowel = ['ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅢ']
consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
noun = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'XSN'] 
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX','EP']

def hae(morph_pos, sentenceType):
    for i in range(len(morph_pos[1])):
        if morph_pos[1][i][1] == 'EC' and morph_pos[1][i - 1][0] == '시':
            morph_pos[1][i][0] = ''
            morph_pos[0][i] = ''
            morph_pos[1][i - 1][0] = ''
            morph_pos[0][i - 1] = ''
             
        # 종결어미를 찾는다.
        if morph_pos[1][i][1] == 'EF' :
            # 전 형태소의 품사가 용언일 때
            if morph_pos[1][i - 1][1] in vb:
                # '하' 불규칙 처리를 위해 따로 빼놓음
                if morph_pos[1][i - 1][0] == '하':
                    morph_pos[0][i] = '아'
                    morph_pos[1][i][0] = '아'
                    continue
                tmp = morph_pos[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if verb[-1] in consonant:
                    # 전 형태소의 모음이 양성일 때
                    if verb[-2] in pos_vowel:
                        morph_pos[0][i] = '아'
                        morph_pos[1][i][0] = '아'
                    # 전 형태소의 모음이 음성일 때    
                    elif verb[-2] in neg_vowel:
                        morph_pos[0][i] = '어'
                        morph_pos[1][i][0] = '어'
                # 전 형태소의 받침이 없고 'ㅏ'나 'ㅓ'로 끝날 때
                elif verb[-2] == 'ㅏ' or verb[-2] == 'ㅓ':
                    morph_pos[0][i] = '어'
                    morph_pos[1][i][0] = '어'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in pos_vowel:
                    morph_pos[0][i] = '아'
                    morph_pos[1][i][0] = '아'
                # 전 형태소의 받침이 없고 모음이 양성일 때
                elif verb[-2] in neg_vowel:
                    morph_pos[0][i] = '어'
                    morph_pos[1][i][0] = '어'
            # 전 형태소가 '아니' 혹은 '이' 일 때
            elif morph_pos[1][i - 1][0] == '아니' or morph_pos[1][i - 1][0] == '이':
                morph_pos[0][i] = '야'
                morph_pos[1][i][0] = '야'
            # 전 형태소의 품사가 체언일 때
            elif morph_pos[1][i - 1][1] in noun:
                tmp = morph_pos[1][i - 1][0]
                verb = hgtk.letter.decompose(tmp[-1])
                # 전 형태소의 받침이 있을 때
                if verb[-1] in consonant:
                    morph_pos[0][i] = '이야'
                    morph_pos[1][i][0] = '이야'
                # 전 형태소의 받침이 없을 때
                else:
                    morph_pos[0][i] = '야'
                    morph_pos[1][i][0] = '야'
    
    return morph_pos # morph, pos 리스트형으로 반환

