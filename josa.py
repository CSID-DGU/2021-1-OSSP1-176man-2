import hgtk
'''
높임/안높임 단어 변환과정에서 조사의 호응을 맞춰주기 위한 함수
조사 전 마지막 글자가 받침이 있는 경우 : 은, 이, 을, 과, 으로(ㄹ제외)
조사 전 마지막 글자가 받침이 없는 경우 : 는, 가, 를, 와, 로
'''


def josa(korlist):

    for i in range(1, len(korlist)):
        # 앞 token이 공백이 아닌 경우
        if korlist[i-1] != " ":
            # '은', '는' 처리
            if(korlist[i][0] == "은" or korlist[i][0] == "는"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(korlist[i-1][len(korlist[i-1])-1]):
                    korlist[i] = "은" + korlist[i][1:]
                # 앞 음절이 받침이 없는 경우
                else:
                    korlist[i] = "는" + korlist[i][1:]
            # '이', '가' 처리
            elif(korlist[i][0] == "이" or korlist[i][0] == "가"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(korlist[i-1][len(korlist[i-1])-1]):
                    korlist[i] = "이" + korlist[i][1:]
                # 앞 음절이 받침이 없는 경우
                else:
                    korlist[i] = "가" + korlist[i][1:]
            # '을', '를' 처리
            elif(korlist[i][0] == "을" or korlist[i][0] == "를"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(korlist[i-1][len(korlist[i-1])-1]):
                    korlist[i] = "을" + korlist[i][1:]
                # 앞 음절이 받침이 없는 경우
                else:
                    korlist[i] = "를" + korlist[i][1:]
            # '과', '와' 처리
            elif(korlist[i][0] == "과" or korlist[i][0] == "와"):
                # 앞 음절이 받침이 있는 경우
                if hgtk.checker.has_batchim(korlist[i-1][len(korlist[i-1])-1]):
                    korlist[i] = "과" + korlist[i][1:]
                # 앞 음절이 받침이 없는 경우
                else:
                    korlist[i] = "와" + korlist[i][1:]
            # '으로', '로' 처리
            elif((korlist[i][0] == "으" and korlist[i][1] == "로") or korlist[i][0] == "로"):
                temp = hgtk.text.decompose(korlist[i-1][len(korlist[i-1])-1])
                # 앞 음절이 받침이 있고 그 받침이 ㄹ이 아닌 경우
                if (hgtk.checker.has_batchim(korlist[i-1][len(korlist[i-1])-1]) and temp[len(temp)-1] != "ㄹ"):
                    korlist[i] = "으로" + korlist[i][1:]
                # 앞 음절이 받침이 없거나 받침이 ㄹ인 경우
                else:
                    korlist[i] = "로" + korlist[i][1:]

    return korlist
