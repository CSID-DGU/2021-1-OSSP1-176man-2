import hgtk


def irregular(sentenceInfo):
    stemStep = stemIrregular(sentenceInfo)
    endingStep = endingIrregular(stemStep)
    sentenceInfo = stemEndingIrregular(endingStep)

    return sentenceInfo


def stemIrregular(sentenceInfo):

    # stem_type: 불규칙 활용 처리 시 '어간'의 형태소 종류
    stem_type = ['VV', 'VA', 'XR']
    ending_type = ['EP', 'EF', 'EC', 'ETM']

    ''' 문장을 구성하는 모든 형태소를 차례로 체크 '''
    for idx in range(len(sentenceInfo[1])):

        ''' 형태소가 '어간'인지 확인 '''
        if sentenceInfo[1][idx][1] in stem_type:

            # stem: '어간' 자모 분리
            stem = list(hgtk.text.decompose(sentenceInfo[1][idx][0]))
            # ending: (문체 변환된 문장)'어미' 자모분리
            ending = list(hgtk.text.decompose(sentenceInfo[1][idx+1][0]))

            ''' 'ㄷ' 불규칙 활용: '어간'의 마지막이 'ㄷ'으로 끝나고 어미'가 '어' 또는 '으니'로 시작한다. '''
            if stem[-2] == 'ㄷ':
                if (ending[0] == 'ㅇ' and ending[1] == 'ㅓ') or (ending[0] == 'ㅇ' and ending[1] == 'ㅡ'):
                    stem[-2] = 'ㄹ'  # 'ㄷ'을 'ㄹ'로 활용시킨다.
                    sentenceInfo[1][idx][0] = hgtk.text.compose(
                        stem)  # 자모합성 후 활용된 어간으로 변환

            ''' 'ㅂ' 불규칙 활용: '어간'의 마지막이 'ㅂ'으로 끝나고 어미'가 '워' 또는 '우니'로 시작한다. '''
            if stem[-2] == 'ㅂ':
                if ((ending[0] == 'ㅇ' and ending[1] == 'ㅓ')):
                    stem = stem[:-2]
                    stem.append('ᴥ')
                    ending[1] = 'ㅝ'
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem)
                    sentenceInfo[1][idx+1][0] = hgtk.text.compose(ending)
                elif ending[0] == 'ㅇ' and ending[1] == 'ㅡ' and ending[3] == 'ㅅ' and ending[4] == 'ㅣ':
                    stem = stem[:-2]
                    stem.append('ᴥ')
                    ending[1] = 'ㅜ'
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem)
                    sentenceInfo[1][idx+1][0] = hgtk.text.compose(ending)
                elif sentenceInfo[1][idx+1][1] in ending_type and ending[0] == 'ㄴ':
                    stem = stem[:-2]
                    stem.append('ᴥ')
                    ending.clear()
                    ending.append('ㅇ')
                    ending.append('ㅜ')
                    ending.append('ㄴ')
                    ending.append('ᴥ')
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem)
                    sentenceInfo[1][idx+1][0] = hgtk.text.compose(ending)

            ''' 'ㅅ' 불규칙 활용: '어간'의 마지막이 'ㅅ'으로 끝나고 어미가 홀소리로 시작한다. '''
            if stem[-2] == 'ㅅ':
                if ending[0] == 'ㅇ':
                    stem = stem[:-2]
                    stem.append('ᴥ')
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem)
                # elif ending[0] == 'ㅇ' and ending[1] == 'ㅡ' and ending[3] == 'ㅅ' and ending[4] == 'ㅣ':
                #     stem = stem[:-2]
                #     stem.append('ᴥ')
                #     sentenceInfo[1][idx][0] = hgtk.text.compose(stem)

            ''' 'ㄹ' 불규칙 활용: 어간이 '_르(+ㄴ)'이 'ㄹ'로 줄고 어미가 '아/어 에서 '라/러'로 바뀐다. '''
            if len(stem) > 3:
                if stem[3] == 'ㄹ' and stem[4] == 'ㅡ' and (ending[1] == 'ㅏ' or ending[1] == 'ㅓ'):
                    stem = stem[:-4]
                    stem.append('ㄹ')
                    stem.append('ᴥ')
                    ending[0] = 'ㄹ'
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem)
                    sentenceInfo[1][idx+1][0] = hgtk.text.compose(ending)

            ''' '우' 불규칙 활용: 푸다->퍼 가 유일 '''
            if stem[0] == 'ㅍ' and stem[1] == 'ㅜ' and ending[1] == 'ㅓ':
                stem[-2] = 'ㅓ'
                sentenceInfo[1][idx][0] = hgtk.text.compose(stem)

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    return sentenceInfo


def endingIrregular(sentenceInfo):

    for i in range(len(sentenceInfo[1])-1):
        if(sentenceInfo[1][i][0][-1] == '하' and sentenceInfo[1][i+1][0] == '아'):
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-1] + '해'
            del(sentenceInfo[1][i + 1])
        elif(sentenceInfo[1][i][0][-1] == '하' and sentenceInfo[1][i+1][0] == '아요'):
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-1] + '해'
            sentenceInfo[1][i+1][0] = "요"
        elif(sentenceInfo[1][i][0][-1] == '하' and sentenceInfo[1][i+1][0] == '았'):
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-1] + '했'
            del(sentenceInfo[1][i + 1])
        elif(sentenceInfo[1][i][0][-2:] == '푸르' and sentenceInfo[1][i+1][0] == '어'):
            sentenceInfo[1][i+1][0] = '러' + sentenceInfo[1][i+1][0][1:]
        elif(sentenceInfo[1][i][0][-2:] == '푸르' and sentenceInfo[1][i+1][0] == '어요'):
            sentenceInfo[1][i+1][0] = '러요' + sentenceInfo[1][i+1][0][1:]
        elif(sentenceInfo[1][i][0][-2:] == '푸르' and sentenceInfo[1][i+1][0][0] == '었'):
            sentenceInfo[1][i+1][0] = '렀' + sentenceInfo[1][i+1][0][1:]

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo


def stemEndingIrregular(sentenceInfo):

    stem = ['VV', 'VA', 'VX', 'VCP', 'VCN']
    ending = ['EP', 'EF', 'EC', 'ETN', 'ETM']

    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.decompose(sentenceInfo[1][i][0])

    # ㅎ 불규칙 활용
    for i in range(len(sentenceInfo[1])):
        if sentenceInfo[1][i][0][-2:] == 'ㅎᴥ' and sentenceInfo[1][i][1] in ['VA'] and sentenceInfo[1][i+1][0][1] == 'ㅓ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-3] + "ㅐᴥ"
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''
        if sentenceInfo[1][i][0][-2:] == 'ㅎᴥ' and sentenceInfo[1][i][1] in ['VA'] and sentenceInfo[1][i+1][0][1] == 'ㅏ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-3] + "ㅔᴥ"
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

    for i in range(len(sentenceInfo[1])):
        if sentenceInfo[1][i][0][-2:] == 'ㅎᴥ' and sentenceInfo[1][i][1] in ['VA'] and (sentenceInfo[1][i+1][0][0] == 'ㄴ' or sentenceInfo[1][i+1][0][0] == 'ㅁ'):
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"

    # 으 규칙 활용
    for i in range(len(sentenceInfo[1])):
        if 'ㅡᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i][1] in stem and sentenceInfo[1][i+1][0][0:2] == 'ㅇㅓ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][: -2] + \
                sentenceInfo[1][i+1][0][1:]
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

    for i in range(len(sentenceInfo[1])):
        if 'ㅡᴥ' in sentenceInfo[1][i][0] and sentenceInfo[1][i][1] in stem and sentenceInfo[1][i+1][0][0:2] == 'ㅇㅏ' and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][: -2] + \
                sentenceInfo[1][i+1][0][1:]
            sentenceInfo[1][i+1][0] = ''
            sentenceInfo[1][i+1][1] = ''

    # ㄹ 규칙 활용
    for i in range(len(sentenceInfo[1])):
        if sentenceInfo[1][i][0] in ['.', '!', '?']:
            break
        if len(sentenceInfo[1][i+1][0]) == 0:
            continue
        if sentenceInfo[1][i][0][-2:] == 'ㄹᴥ' and sentenceInfo[1][i+1][0][0] in ['ㄴ', 'ㅅ', 'ㅂ'] and sentenceInfo[1][i+1][1] in ending:
            sentenceInfo[1][i][0] = sentenceInfo[1][i][0][:-2] + "ᴥ"

    for i in range(len(sentenceInfo[1])):
        sentenceInfo[1][i][0] = hgtk.text.compose(sentenceInfo[1][i][0])

    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))

    return sentenceInfo
