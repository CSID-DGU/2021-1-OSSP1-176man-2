from konlpy.tag import Komoran


def Spacing(posList):
    komoran = Komoran()
    space = ['JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JC', 'JX', 'EP', 'EF', 'EC',
             'ETN', 'ETM', 'XSN', 'XSV', 'XSA', 'SF', 'SP', 'VCP', 'VCN']  # 띄어쓰기를 하지 않는 품사들을 저장한 리스트

    list = []
    # 각 낱말을 리스트에 합성하여 문장으로 만들어준다.
    for i in range(len(posList)):
        list.append(posList[i][0])

        if (i == len(posList) - 1):
            break
        else:
            # 조사와 연결어미 등 띄어쓰기를 하지 않는 품사들의 정보를 통해 띄어쓰기 처리를 해준다.
            if (posList[i + 1][1] in space):
                continue
            else:
                list.append(" ")

    return list  # 재합성한 하나의 문장 출력
