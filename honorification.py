import hgtk
'''
input morph, pos, flag 리스트
output morph, pos, flag 리스트
주체 높임에 따른 '시' 추가 및 삭제
'''


def honorification1(sentenceInfo):

    stem_type = ['VV', 'VA', 'VX', 'VCP', 'VCN', 'XSN', 'XSV', 'XSA', 'XR']

    if sentenceInfo[2][0] == 1:
        i = 0
        while i < len(sentenceInfo[1]):
            if sentenceInfo[1][i][0] == '으시' and (sentenceInfo[1][i][1] == 'EC' or sentenceInfo[1][i][1] == 'EP'):
                sentenceInfo[1][i] = '시'
                if sentenceInfo[1][i + 1][0] == '시' and (sentenceInfo[1][i][1] == 'EC' or sentenceInfo[1][i][1] == 'EP'):
                    del(sentenceInfo[1][i + 1])
            elif (sentenceInfo[1][i][1] == 'EF'):
                for j in range(i - 1, 0, -1):
                    if sentenceInfo[1][j][1] in stem_type:
                        stem = sentenceInfo[1][j][0]
                        if (stem == '위하' or stem == '대하') and sentenceInfo[1][i][1] == 'EC':
                            break
                        if sentenceInfo[1][j+1][0] == '시':
                            break
                        sentenceInfo[1].insert(j + 1, ['시', 'EP'])
                        i += 1
                        break
            i += 1

    elif sentenceInfo[2][0] == 0:
        i = 0
        while i < len(sentenceInfo[1]):
            if (sentenceInfo[1][i][0] == '시' or sentenceInfo[1][i][0] == '으시') and (sentenceInfo[1][i][1] == 'EC' or sentenceInfo[1][i][1] == 'EP'):
                del(sentenceInfo[1][i])
            i += 1

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    return sentenceInfo  # morph, pos 리스트형으로 반환


def honorification2(sentenceInfo):
    stem_type = ['VV', 'VA', 'VX', 'VCP', 'VCN', 'XSN', 'XSV', 'XSA', 'XR']

    for i in range(len(sentenceInfo[1])-1, 0, -1):
        if sentenceInfo[1][i][0] == '시' and (sentenceInfo[1][i][1] == 'EC' or sentenceInfo[1][i][1] == 'EP'):
            if hgtk.checker.has_batchim(sentenceInfo[1][i-1][0][-1]):
                sentenceInfo[1][i][0] = '으시'
    return sentenceInfo
