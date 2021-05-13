import pandas as pd

''' xlrd, pandas, openpyxl 모듈 설치하고 진행 '''

# pd.set_option('display.max_rows', None)  # row 생략 없이 출력
# pd.set_option('display.max_columns', None)  # col 생략 없이 출력

excelTitle = "" + "1_구어체(1)_200226"  # 경로 + 파일명
excel_dafaframe = pd.read_excel(excelTitle + ".xlsx", engine='openpyxl')  # 원본 excel 파일
original_eng_list = list((excel_dafaframe['번역문']))  # 영어 문장 (번역문)
original_kor_list = list((excel_dafaframe['원문']))  # 한국어 문장 (원문)

# example
print(original_eng_list[0])
print(original_kor_list[0])
