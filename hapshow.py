import hgtk

'''
    input으로 들어온 번역된 문장을 분석하여 종결어미 부분을 합쇼체의 종결어미로 변경해준다.
'''


def hapshow(Analyzerlist, sentenceType):
    # word_class : 어미 변경시 변경되어야 할 품사(종결어미)를 저장한 배열
    word_class = ["EF"]

    # tuple의 값이 변경가능하도록 list 형식으로 변경
    Analyzerlist[1] = list(map(list, Analyzerlist[1]))

    # 평서문인 경우
    if sentenceType == "statement":
        for i in range(len(Analyzerlist[1])):
            # 종결 어미를 찾은 경우
            if Analyzerlist[1][i][1] in word_class:
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(Analyzerlist[1][i-1][0][len(Analyzerlist[1][i-1][0])-1]):
                    Analyzerlist[1][i][0] = "습니다"
                    Analyzerlist[0][i] = "습니다"
                # 앞 음절이 받침이 없는 경우
                else:
                    Analyzerlist[1][i][0] = "ㅂ니다"
                    Analyzerlist[0][i] = "ㅂ니다"

    # 의문문인 경우
    elif sentenceType == "question":
        for i in range(len(Analyzerlist[1])):
            # 종결 어미를 찾은 경우
            if Analyzerlist[1][i][1] in word_class:
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(Analyzerlist[1][i-1][0][len(Analyzerlist[1][i-1][0])-1]):
                    Analyzerlist[1][i][0] = "습니까"
                    Analyzerlist[0][i] = "습니까"
                # 앞 음절이 받침이 없는 경우
                else:
                    Analyzerlist[1][i][0] = "ㅂ니까"
                    Analyzerlist[0][i] = "ㅂ니까"

    # 명령형인 경우
    elif sentenceType == "command":
        for i in range(len(Analyzerlist[1])):
            # 종결 어미를 찾은 경우
            if Analyzerlist[1][i][1] in word_class:
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(Analyzerlist[1][i-1][0][len(Analyzerlist[1][i-1][0])-1]):
                    Analyzerlist[1][i][0] = "으십시오"
                    Analyzerlist[0][i] = "으십시오"
                # 앞 음절이 받침이 없는 경우
                else:
                    Analyzerlist[1][i][0] = "십시오"
                    Analyzerlist[0][i] = "십시오"

    return Analyzerlist
