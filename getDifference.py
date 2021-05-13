from konlpy.tag import Komoran

komoran = Komoran() 

'''
- 형태소 분석 후 이를 합성하는 기능은 생략
- 비교할 두 개의 문장은 임의로 지정
- 두 개의 문장은 띄어쓰기로 구분된 단어의 일치 여부로 비교

str1_list, str2_list : 띄어쓰기로 구분된 단어들을 저장하는 list
                       ex) ["그리고", "나와", "내", ...]

return : 비교 수행 시 일치하지 않는 단어들의 쌍들을 각각 tuple로 저장하는 list 반환
'''

def get_difference(str1, str2):
    str1_list     = []  # 띄어쓰기로 구분된 list  
    str2_list     = []  # (ex) ["그리고", "나와",...]
    diff_list     = []  # 반환할 배열
    marks         = [" ", ".", "!", "?"] # 문장부호 list (띄어쓰기 포함)

    tmp = ""
    # 첫 번째 문장에서 띄어쓰기로 구분된 단어들을 list에 저장
    for s in str1:
        if s in marks:
            str1_list.append(tmp)  # 띄어쓰기를 만나면 임시 저장된 글자들 삽입
            tmp = ""
        else:
            tmp += s  # 띄어쓰기를 만날 때 까지 각 글자 임시 저장
            
    tmp = ""
    # 두 번째 문장에서 띄어쓰기로 구분된 단어들을 list에 저장
    for s in str2:
        if s in marks:
            str2_list.append(tmp)  # 띄어쓰기를 만나면 임시 저장된 글자들 삽입
            tmp = ""
        else:
            tmp += s  # 띄어쓰기를 만날 때 까지 각 글자 임시 저장

    
    # exception: 형태소 분석 후 합성이 잘못되었을 때 -1 반환
    if len(str1_list) != len(str2_list):
        return -1

    # 두 list의 각 원소(단어) 비교
    for s1, s2 in zip(str1_list, str2_list):
        if s1 != s2:
            diff_list.append((s1, s2))
    
    return diff_list
    

original = "그리고 나와 내 개들의 사진을 보내줄게." # 원본 문장
composed = "그리고 나오아 내 개들의 사진을 보내어줄게." # 형태소 분석 후 재합성된 문장

difference_list = get_difference(original, composed)

print(difference_list)
