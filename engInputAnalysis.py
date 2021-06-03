import nltk


'''
input 영어 문장에 대해서
(1) 물음표로 끝나면 -> 의문문(question)
(2) 첫번째 단어가 동사이고, 뒤가 .이거나 ! -> 명령문(command)
(3) 첫번째 단어가 동사가 아니고 뒤가 . -> 평서문(statement)
nltk 오픈소스 활용
nltk.word_tokenize() : 영어문장을 토근화
nltk.pos_tag : 토큰한 단어에 따라 품사 지정
'''


def sentenceType(inputEng):

    tokens = nltk.word_tokenize(inputEng)
    tags = nltk.pos_tag(tokens)

    # nltk에서 get의 품사를 명사로 보아 예외처리.
    exceptWord = ["Get", "get", "Turn", "turn"]

    # 첫 단어가 접속사/전치사이면, ',' 별로 문장을 나누어 . ! 가 있는 문장에서 맨 앞 품사를 확인
    if tags[0][1] in ["IN", "WRB"] and tags[-1][0] != "?":
        splitList = []
        tmp = []

        for t in tags:
            if t[0] in ['.', '!', ',']:
                tmp.append(t)
                splitList.append(tmp)
                tmp = []
            else:
                tmp.append(t)

        for l in splitList:
            if ('.', '.') in l or ('!', '!') in l:
                firstWord = l[0]
                break

        if "VB" in firstWord[1] or firstWord[0] in exceptWord:
            return "command"
        else:
            return "statement"

    # 맨 앞이 접속사/전치사가 아니면
    else:
        if inputEng[-1] == '?':
            return "question"

        elif (inputEng[-1] in ['.', '!'] and "VB" in tags[0][1]) or tags[0][0] in exceptWord:
            return "command"
        # 첫 단어가 동사가 아닌 부사가 오더라도, 부사+동사 or 부사+,+동사 인지 확인하여 명령문 처리
        elif 'RB' in tags[0][1] and ("VB" in tags[1][1] or (tags[1][1] is "," and "VB" in tags[2][1])):
            return "command"

        elif inputEng[-1] in ['.', '!'] and "VB" not in tags[0][1]:
            return "statement"

        else:
            return "etc"
