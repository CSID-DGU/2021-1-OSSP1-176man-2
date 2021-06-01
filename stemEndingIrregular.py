import main
import hgtkTest
import hgtk

'''
'ㄷ', 'ㅂ', 'ㅅ', '르', '우' 에 대한 불규칙 변형 처리

2021-05-26 
- '르' 처리 제외 초안 작성 완료

2021-06-01 (1차 수정)
- 문체 변환 반영
- 어미에 따라 어간 변환 여부를 결정하도록 수정
- 'ㄷ', 'ㅅ' 제외 세부 수정 필요

2021-06-01 (2차 수정)
- 'ㅂ', '르', '우' 수정 완료

2021-06-01 (3차 수정)
- '시' 또는 '으시' 처리 추가 (수정 필요)

@param kor_list : Papago 번역이 완료된 한글 문장
@param sentenceInfo : 문체 변환이 완료된 한글 문장

활용되지 않은 어간일 때 활용 처리
ex) 걷(다) -> 걸(어)
ex) 가볍(다) -> 가벼(워)
ex) 긋(다) -> 그(어)
ex) 누르(다) -> 눌(러)
ex) 푸다 -> 퍼

'''


def stemIrregular(sentenceInfo):

    # stem_type: 불규칙 활용 처리 시 '어간'의 형태소 종류
    stem_type = ['VV', 'VA', 'XR']

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
                if (ending[0] == 'ㅇ' and ending[1] == 'ㅓ') or (ending[0] == 'ㅇ' and ending[1] == 'ㅡ' ):
                    stem[-2] = 'ㄹ' # 'ㄷ'을 'ㄹ'로 활용시킨다.
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem) # 자모합성 후 활용된 어간으로 변환

            ''' 'ㅂ' 불규칙 활용: '어간'의 마지막이 'ㅂ'으로 끝나고 어미'가 '워' 또는 '우니'로 시작한다. '''
            if stem[-2] == 'ㅂ':
                if ((ending[0] == 'ㅇ' and ending[1] == 'ㅓ')):
                    stem = stem[:-2]
                    stem.append('ᴥ')
                    ending[1] = 'ㅝ'
                    sentenceInfo[1][idx][0] = hgtk.text.compose(stem)
                    sentenceInfo[1][idx+1][0] =  hgtk.text.compose(ending)
                if ending[0] == 'ㅇ' and ending[1] == 'ㅡ' and ending[3] == 'ㅅ' and ending[4] == 'ㅣ':
                    stem = stem[:-2]
                    stem.append('ᴥ')
                    ending[1] = 'ㅜ'
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
            if stem[0] == 'ㅍ' and stem[1] == 'ㅜ':
                stem[-2] = 'ㅓ'
                sentenceInfo[1][idx][0] = hgtk.text.compose(stem)


    sentenceInfo[0] = list(map(lambda x: x[0], sentenceInfo[1]))
    return sentenceInfo



korList = main.sentenceInfoList[0]
print("번역 및 형태소 분석 : ", korList[1])

sentenceHae = main.sentenceHae
sentenceHaera = main.sentenceHaera
sentenceHaeyo = main.sentenceHaeyo
sentenceHapshow = main.sentenceHapshow
print("해 체 변환 : ", sentenceHae[1])
print("해라 체 변환 : ", sentenceHaera[1])
print("해요 체 변환 : ", sentenceHaeyo[1])
print("합쇼 체 변환 : ", sentenceHapshow[1])

stemIrregularHae = stemIrregular(sentenceHae)
stemIrregularHaera = stemIrregular(sentenceHaera)
stemIrregularHaeyo = stemIrregular(sentenceHaeyo)
stemIrregularHapshow = stemIrregular(sentenceHapshow)
print("불규칙 활용 (해): ", stemIrregularHae[0])
print("불규칙 활용 (해라): ", stemIrregularHaera[0])
print("불규칙 활용 (해요): ", stemIrregularHaeyo[0])
print("불규칙 활용 (합쇼): ", stemIrregularHapshow[0])

outputSentence = []
outputSentence.append(hgtkTest.textCompose(stemIrregularHae[0]))
outputSentence.append(hgtkTest.textCompose(stemIrregularHaera[0]))
outputSentence.append(hgtkTest.textCompose(stemIrregularHaeyo[0]))
outputSentence.append(hgtkTest.textCompose(stemIrregularHapshow[0]))
print(outputSentence)
