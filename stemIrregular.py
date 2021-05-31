import main
import copy
import hgtk

'''
'ㄷ', 'ㅂ', 'ㅅ', '르', '우' 에 대한 불규칙 변형 처리

2021-05-26 
- '르' 처리 제외 초안 작성 완료

2021-06-01
- 문체 변환 반영
- 어미에 따라 어간 변환 여부를 결정하도록 수정
- 'ㄷ', 'ㅅ' 제외 세부 수정 필요

@param kor_list : Papago 번역이 완료된 한글 문장
@param style_transform_list : 문체 변환이 완료된 한글 문장

활용되지 않은 어간일 때 활용 처리
ex) 걷(다) -> 걸(어)
ex) 가볍(다) -> 가벼(워)
ex) 긋(다) -> 그(어)
ex) 누르(다) -> 눌(러)
ex) 푸다 -> 퍼

'''


def stemIrregular(kor_list, style_transform_list):

    # stem_type: 불규칙 활용 처리 시 '어간'의 형태소 종류
    stem_type = ['VV', 'VA', 'XR']
    ending_type = ['EP', 'EF', 'EC']

    # 문체 변환된 문장을 deepcopy하여 반환할 문장으로 저장
    return_sentence = copy.deepcopy(style_transform_list)

    ''' 문장을 구성하는 모든 형태소를 차례로 체크 '''
    for idx in range(len(kor_list[1])):

        ''' 형태소가 '어간'인지 확인 '''
        if kor_list[1][idx][1] in stem_type:
            
            # stem: '어간' 자모 분리
            stem = list(hgtk.text.decompose(kor_list[1][idx][0]))
            # ending: (문체 변환된 문장)'어미' 자모분리
            ending = list(hgtk.text.decompose(style_transform_list[1][idx+1][0]))

            ''' 'ㄷ' 불규칙 활용: '어간'의 마지막이 'ㄷ'으로 끝나고 어미'가 '어' 또는 '으니'로 시작한다. '''
            if stem[-2] == 'ㄷ' and ((ending[0] == 'ㅇ' and ending[1] == 'ㅓ')): # or (ending[0] == 'ㅇ' and ending[1] == 'ㅡ' and ending[3] == 'ㄴ' and ending[4] == 'ㅣ')):
                stem[-2] = 'ㄹ' # 'ㄷ'을 'ㄹ'로 활용시킨다.
                return_sentence[1][idx][0] = hgtk.text.compose(stem) # 자모합성 후 활용된 어간으로 변환

            ''' 'ㅂ' 불규칙 활용: '어간'의 마지막이 'ㅂ'으로 끝나고 어미'가 '워' 또는 '우니'로 시작한다. '''
            if stem[-2] == 'ㅂ' and ((ending[0] == 'ㅇ' and ending[1] == 'ㅓ')): # and ending[1] == 'ㅓ') or (ending[0] == 'ㅇ' and ending[1] == 'ㅜ' and ending[3] == 'ㄴ' and ending[4] == 'ㅣ')):
                stem = stem[:-2]
                stem.append('ᴥ')
                ending.insert(1, 'ㅜ')
                return_sentence[1][idx][0] = hgtk.text.compose(stem)
                return_sentence[1][idx+1][0] =  hgtk.text.compose(ending)

            ''' 'ㅅ' 불규칙 활용: '어간'의 마지막이 'ㅅ'으로 끝나고 어미가 홀소리로 시작한다. '''
            if stem[-2] == 'ㅅ' and ending[0] == 'ㅇ':
                stem = stem[:-2]
                stem.append('ᴥ')
                return_sentence[1][idx][0] = hgtk.text.compose(stem) 
            
            ''' 'ㄹ' 불규칙 활용: 어간이 '_르(+ㄴ)'이 'ㄹ'로 줄고 어미가 '아/어 에서 '라/러'로 바뀐다. '''
            if stem[3] == 'ㄹ' and stem[4] == 'ㅡ' and (ending[1] == 'ㅏ' or ending[1] == 'ㅓ'):
                stem = stem[:-3]
                stem.append('ㄹ')
                stem.append('ᴥ')
                ending[0] = 'ㄹ'
                return_sentence[1][idx][0] = hgtk.text.compose(stem)
                return_sentence[1][idx+1][0] = hgtk.text.compose(ending)

            ''' '우' 불규칙 활용: 푸다->퍼 가 유일 '''
            if stem[0] == 'ㅍ' and stem[1] == 'ㅜ':
                stem[-2] = 'ㅓ'
                return_sentence[1][idx][0] = hgtk.text.compose(stem)

    return return_sentence



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

stemIrregularHae = stemIrregular(korList, sentenceHae)
stemIrregularHaera = stemIrregular(korList, sentenceHaera)
stemIrregularHaeyo = stemIrregular(korList, sentenceHaeyo)
stemIrregularHapshow = stemIrregular(korList, sentenceHapshow)
print("불규칙 활용 (해): ", stemIrregularHae[1])
print("불규칙 활용 (해라): ", stemIrregularHaera[1])
print("불규칙 활용 (해요): ", stemIrregularHaeyo[1])
print("불규칙 활용 (합쇼): ", stemIrregularHapshow[1])
