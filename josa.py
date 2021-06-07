import hgtk
'''
높임/안높임 단어 변환과정에서 조사의 호응을 맞춰주기 위한 함수
조사 전 마지막 글자가 받침이 있는 경우 : 은, 이, 을, 과, 으로(ㄹ제외)
조사 전 마지막 글자가 받침이 없는 경우 : 는, 가, 를, 와, 로
'''
pos_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅛ']
neg_vowel = ['ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅚ', 'ㅙ',
             'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅢ']
consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ',
             'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
noun = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'XSN']
vb = ['VV', 'VA', 'XSV', 'XSA', 'VX', 'EP']
check = ['EC', 'EP', 'EF', 'JKS', 'JKC', 'JKG',
         'JKO', 'JKB', 'JKV', 'JKQ', 'JC', 'JX']


def josa(sentenceInfo):

    for i in range(1, len(sentenceInfo[1])):
        # 앞 token이 공백이 아닌 경우
        if sentenceInfo[1][i-1][0] != " " and sentenceInfo[1][i][1] in check:

            vowelCheck = hgtk.letter.decompose(sentenceInfo[1][i-1][0][-1])

            # '은', '는' 처리
            if(sentenceInfo[1][i][0] == "은" or sentenceInfo[1][i][0] == "는"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]):
                    sentenceInfo[1][i][0] = "은"
                # 앞 음절이 받침이 없는 경우
                else:
                    sentenceInfo[1][i][0] = "는"
            # '이', '가' 처리
            elif(sentenceInfo[1][i][0] == "이" or sentenceInfo[1][i][0] == "가"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]):
                    sentenceInfo[1][i][0] = "이"
                # 앞 음절이 받침이 없는 경우
                else:
                    sentenceInfo[1][i][0] = "가"
            # '을', '를' 처리
            elif(sentenceInfo[1][i][0] == "을" or sentenceInfo[1][i][0] == "를"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]):
                    sentenceInfo[1][i][0] = "을"
                # 앞 음절이 받침이 없는 경우
                else:
                    sentenceInfo[1][i][0] = "를"
            # '과', '와' 처리
            elif(sentenceInfo[1][i][0] == "과" or sentenceInfo[1][i][0] == "와"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]):
                    sentenceInfo[1][i][0] = "과"
                # 앞 음절이 받침이 없는 경우
                else:
                    sentenceInfo[1][i][0] = "와"
            # '으로', '로' 처리
            elif(sentenceInfo[1][i][0] == "으로" or sentenceInfo[1][i][0] == "로"):
                temp = hgtk.text.decompose(
                    sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1])
                # 앞 음절이 받침이 있고 그 받침이 ㄹ이 아닌 경우
                if (hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][len(sentenceInfo[1][i-1][0])-1]) and temp[len(temp)-1] != "ㄹ"):
                    sentenceInfo[1][i][0] = "으로"
                # 앞 음절이 받침이 없거나 받침이 ㄹ인 경우
                else:
                    sentenceInfo[1][i][0] = "로"

            # '아', '어' 처리
            elif(sentenceInfo[1][i][0] == "아" or sentenceInfo[1][i][0] == "어"):
                # 앞 음절의 모음이 양성인 경우
                if vowelCheck[1] in pos_vowel and vowelCheck[2] != "ㅆ":
                    sentenceInfo[1][i][0] = "아"
                # 앞 음절의 모음이 음성인 경우
                else:
                    sentenceInfo[1][i][0] = "어"
            # '았', '었' 처리
            elif(sentenceInfo[1][i][0] == "았" or sentenceInfo[1][i][0] == "었"):
                # 앞 음절의 모음이 양성인 경우
                if vowelCheck[1] in pos_vowel and vowelCheck[2] != "ㅆ":
                    sentenceInfo[1][i][0] = "았"
                # 앞 음절의 모음이 음성인 경우
                else:
                    sentenceInfo[1][i][0] = "었"
            # '아요', '어요' 처리
            elif(sentenceInfo[1][i][0] == "아요" or sentenceInfo[1][i][0] == "어요"):
                # 앞 음절의 모음이 양성인 경우
                if vowelCheck[1] in pos_vowel and vowelCheck[2] != "ㅆ":
                    sentenceInfo[1][i][0] = "아요"
                # 앞 음절의 모음이 음성인 경우
                else:
                    sentenceInfo[1][i][0] = "어요"

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo
