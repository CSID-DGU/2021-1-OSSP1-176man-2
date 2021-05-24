import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hae
import haera
import haeyo
import hapshow

# 사용자가 영어문장과 문체를 선택해서 입력
print("번역할 영어문장을 입력해주세요(문법적으로 완벽한 문장): ")
inputSentence = input()
print("번역된 문장의 문체를 선택해주세요(해, 해라, 해요, 합쇼): ")
inputSentenceType = input()

sentenceType = engInputAnalysis.sentenceType(inputSentence) # 문장종류 확인
inputAnalyzer = naverPapago.translate(inputSentence) # 파파고API로 번역 및 Komoran으로 형태소 분석
morph_pos = komoranSpacing.Spacing(inputAnalyzer[1]) # 분석된 형태소를 이용하여 띄어쓰기 처리

# 사용자가 선택한 문체에 맞는 함수 실행후 어미 변경
changeEnding = [] # 어미 변경 후 morph, pos 리스트 저장할 변수
if inputSentenceType == '해':
    changeEnding = hae.hae(morph_pos)
elif inputSentenceType == "해라":
    changeEnding = haera.haera(morph_pos, sentenceType)
elif inputSentenceType == "해요":
    changeEnding = haeyo.haeyo(morph_pos, sentenceType)
elif inputSentenceType == "합쇼":
     changeEnding = hapshow.hapshow(morph_pos, sentenceType)
else:
    print("error")
    exit(1)

# 가장 마지막 부분으로 hgtk를 이용하여 재합성하여 출력
completeSentence = hgtkTest.textCompose(changeEnding[0])
print(completeSentence)