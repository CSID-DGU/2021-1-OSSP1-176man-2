import hgtk

def hae(first_res):
    pos_bowel = ['ㅏ','ㅗ','ㅑ','ㅛ','ㅘ','ㅚ','ㅐ']
    neg_bowel = ['ㅓ','ㅜ','ㅕ','ㅠ','ㅔ','ㅝ','ㅖ','ㅡ']
    for i in range(len(first_res[1])):
        
        if first_res[1][i][1] == 'VV' and (first_res[1][i + 1][1] == 'EF' or first_res[1][i + 2][1] == 'EF') :
            if first_res[1][i + 1][0] == 'ㄴ다' and len(hgtk.text.decompose(first_res[1][i][0])) == 4:
                first_res[0][i + 1] = '아'
                break
            if first_res[1][i + 1][0] == 'ㄴ다' and len(hgtk.text.decompose(first_res[1][i][0])) == 3:
                first_res[0][i + 1] = ''
                break
            '''
            if '모르' in first_res[1][i][0]:
                first_res[0][i] = '모'
                first_res[0][i + 1] = 'ㄹ라'
                break
            if '흐르' in first_res[1][i][0]:
                first_res[0][i] = '흐'
                first_res[0][i + 1] = 'ㄹ러'
                break
            else: 
                first_res[0][i + 1] = ''
                first_res[0][i + 2] = ''
                break
            '''   
        #종결어미에 따른 '-해'체 변환
        '''
        if first_res[1][i][1] == 'EF' and first_res[1][i][0] == '다':
            first_res[0][i] = '어'
            first_res[1][i][0] = '어'
            break
        '''
        '''
        if first_res[1][i][1] == 'EF' and first_res[1][i][0] == '어요':
            first_res[0][i] = '어'
            first_res[1][i][0] = '어'
            break
        '''
        if first_res[1][i][1] == 'EF' and first_res[1][i][0] == 'ㄹ까요':
            first_res[0][i] = '야'
            first_res[1][i][0] = '야'
            break
        #모음 조화현상에 따른 '-해'체 어미 변환
        elif first_res[1][i][1] == 'EF' and first_res[1][i - 1][0] == '시' and first_res[1][i - 2][1] == 'VV':
            first_res[0][i - 1] = ''
            first_res[1][i - 1][0]= ''
            first_res[1][i - 1][1]= ''
            if hgtk.text.decompose(first_res[1][i - 2][0])[1] in pos_bowel:
                first_res[0][i] = '아'
                first_res[1][i][0] = '아'
                break
            elif hgtk.text.decompose(first_res[1][i - 2][0])[1] in neg_bowel:
                first_res[0][i] = '어'
                first_res[1][i][0] = '어'
                break
        elif first_res[1][i][1] == 'EF' and first_res[1][i - 1][1] == 'VV':
            if hgtk.text.decompose(first_res[1][i-1][0])[1] in pos_bowel:
                first_res[0][i] = '아'
                first_res[1][i][0] = '아'
                break
            elif hgtk.text.decompose(first_res[1][i-1][0])[1] in neg_bowel:
                first_res[0][i] = '어'
                first_res[1][i][0] = '어'
                break
        elif first_res[1][i][1] == 'EF':
            first_res[0][i] = '어'
            first_res[1][i][0] = '어'
            break
        #명사+'하'의 합성으로 동사가 되는 부분에 대해서의 '-해'체 변환
        if first_res[1][i][1] == 'NNG' and first_res[1][i + 1][0] == '하':
            first_res[0][i + 1] = '해'
            first_res[0][i + 2] = ''
            first_res[1][i + 1][0] = '해'
            first_res[1][i + 2][0] = ''
            first_res[1][i + 2][1] = ''
            break
        elif first_res[1][i][1] == 'NNG' and first_res[1][i + 1][0] == '하' and first_res[1][i + 2][0] == '시':
            first_res[0][i + 1] = '해'
            first_res[0][i + 2] = ''
            first_res[0][i + 3] = ''
            first_res[1][i + 1][0] = '해'
            first_res[1][i + 2][0] = ''
            first_res[1][i + 3][0] = ''
            first_res[1][i + 2][1] = ''
            first_res[1][i + 3][1] = ''
            break
        #명사 + VCP + EF 의 합성으로 문장이 끝나는 경우에 대해서의 '-해'체 변환
        if first_res[1][i][1] == 'NNP' and (first_res[1][i + 1][1] =='EF' or first_res[1][i + 2][1] == 'EF'):
            first_res[0][i + 1] = '야'
            first_res[0][i + 2] = ''
            first_res[1][i + 1][0] = '야'
            first_res[1][i + 2][0] = ''
            first_res[1][i + 2][1] = ''
            break
        elif first_res[1][i][1] == 'NNP' and first_res[1][i + 2][1] == 'EF' and first_res[1][i + 2][0] == 'ㅂ니다':
            first_res[0][i + 1] = '야'
            first_res[0][i + 2] = ''
            first_res[1][i + 1][0] = '야'
            first_res[1][i + 2][0] = ''
            first_res[1][i + 2][1] = ''
            break
        #모음 조화현상에 따른 '-해'체 어미 변환
        if first_res[1][i][1] == 'EF' and first_res[1][i - 1][1] == 'VV':
            if hgtk.text.decompose(first_res[1][i-1][0]) in pos_bowel:
                first_res[0][i] = '아'
                first_res[1][i][0] = '아'
            elif hgtk.text.decompose(first_res[1][i-1][0]) in neg_bowel:
                first_res[0][i] = '어'
                first_res[1][i][0] = '어'
    return first_res    