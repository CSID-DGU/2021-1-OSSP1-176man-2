'''
불규칙 활용 중 어미의 불규칙을 처리하기 위한 함수
어미의 불규칙 :
            '여' 불규칙 : '하' + '아' 처리 완료
            '러' 불규칙 : '푸르' + '어' 처리 완료 / '이르' + '어' 처리의 경우 어떤 의미의 이르에 해당하는지를 확인해야하므로 DB처리 과정 중에 받아온 flag변수를 이용하여 처리
            '오' 불규칙 : 문체에 맞는 어미 변환을 먼저 처리해준 이후에 진행되므로 처리 불필요
'''


def endingIrregular(sentenceInfo):

    for i in range(len(sentenceInfo)-1):
        if(sentenceInfo[i][len(sentenceInfo[i])-1] == '하' and sentenceInfo[i+1][0] == '아'):
            sentenceInfo[i+1] = '여' + sentenceInfo[i+1][1:]
        elif(sentenceInfo[i][len(sentenceInfo[i])-2:] == '푸르' and sentenceInfo[i+1][0] == '어'):
            sentenceInfo[i+1] = '러' + sentenceInfo[i+1][1:]
        # 동음이의어 처리 추가 필요
        elif(sentenceInfo[i][len(sentenceInfo[i])-2:] == '이르' and sentenceInfo[i+1][0] == '어'):
            sentenceInfo[i+1] = '러' + sentenceInfo[i+1][1:]

    return sentenceInfo
