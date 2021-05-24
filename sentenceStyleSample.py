import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis

'''
    print는 각 변수에 어떤 값들이 들어가 있는지 확인하기 위해 씀.
    만약 문체에 따른 어미 변환 코드를 작성할 때는 새로운 file(.py)를 생성하고
    여기 있는 주석 다 빼고 print 다 빼고 진행하면 될거 같습니다.
'''

# papago의 input으로 들어갈 영어문장
inputSentence = input()

# 입력된 영어문장의 종류 🠒 return : statement, question, command
sentenceType = engInputAnalysis.sentenceType(inputSentence)
print(sentenceType)

# 입력된 영어문장을 파파고로 번역 🠒 return : 번역된 한국어에 대한 komoran 분석(이중list) 🠒 [komoran.morphs(korText), komoran.pos(korText)]
inputAnalyzer = naverPapago.translate(inputSentence)
print(inputAnalyzer[0])

# 입력으로 komoran.pos(korText) 받아, 품사에 따른 띄어쓰기 처리 🠒 return : 띄어쓰기가 반영된 분석(이중list) 🠒 [komoran.morphs(), komoran.pos()]
first_res = komoranSpacing.Spacing(inputAnalyzer[1])

# 띄어쓰기를 포함한 komoran.pos() (띄어쓰기는 'BLK'로 처리.)
# ex) [('아이', 'NNG'), ('들', 'XSN'), ('을', 'JKO'), (' ', 'BLK'), ('위하', 'VV'), ('아', 'EC')]
print(first_res[1])

# 띄어쓰기 처리된 list를 받아 합성. 🠒 return : string
second_res = hgtkTest.textCompose(first_res[0])
print(second_res)  # 띄어쓰기 처리된 string
