import hae
import haera
import haeyo
import hapshow
import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis

inputSentence = input()
sentenceType = engInputAnalysis.sentenceType(inputSentence)
inputAnalyzer = naverPapago.translate(inputSentence)
Analyzerlist1 = komoranSpacing.Spacing(inputAnalyzer[1])
Analyzerlist2 = komoranSpacing.Spacing(inputAnalyzer[1])
Analyzerlist3 = komoranSpacing.Spacing(inputAnalyzer[1])
Analyzerlist4 = komoranSpacing.Spacing(inputAnalyzer[1])

print("해체 : ")
print(hae.hae(Analyzerlist1))
print(hgtkTest.textCompose(hae.hae(Analyzerlist1)[0]))
print("\n")
print("해라체 : ")
print(haera.haera(Analyzerlist2, sentenceType))
print(hgtkTest.textCompose(haera.haera(Analyzerlist2, sentenceType)[0]))
print("\n")
print("해요체 : ")
print(haeyo.haeyo_ver1(Analyzerlist3, sentenceType))
print(hgtkTest.textCompose(haeyo.haeyo_ver1(Analyzerlist3, sentenceType)[0]))
print("\n")
print("합쇼체 : ")
print(hapshow.hapshow(Analyzerlist4, sentenceType))
print(hgtkTest.textCompose(hapshow.hapshow(Analyzerlist4, sentenceType)[0]))
