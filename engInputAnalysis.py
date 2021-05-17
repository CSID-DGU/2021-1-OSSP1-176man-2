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

    if inputEng[-1] == '?':
        return "question"
    elif inputEng[-1] in ['.', '!'] and "VB" in tags[0][1]:
        return "command"
    elif inputEng[-1] in ['.', '!'] and "VB" not in tags[0][1]:
        return "statment"
    else:
        return "etc"
