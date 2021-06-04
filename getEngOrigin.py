from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

lm = WordNetLemmatizer()

tag = [wordnet.ADJ, wordnet.VERB, wordnet.NOUN, wordnet.ADV]

'''
- 단어의 원형을 찾는 함수 lemmatize()를 위해 단어의 품사를 변형시켜주는 함수
- 불규칙 용언의 정보가 주어지면 DB에 삽입 또는 변경하기 위해 이루어지는 전체적인 DB 처리를 포함
@param treebank_tag : 각 영단어의 품사
return : 변형된 영단어의 품사
'''


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N') or treebank_tag.startswith('P'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return treebank_tag


'''
- 영어 문장을 구성하는 형태소들의 단어를 원형으로 복구시키는 함수
@param inputSentence : 사용자가 입력한 영어 문장
return : 각 단어가 원형으로 변환된 후의 영단어 list
'''


def get_eng_origin(inputSentence):
    tokens = nltk.word_tokenize(inputSentence)
    tags = nltk.pos_tag(tokens)
    for idx, t in enumerate(tags):
        if t[0] == 'ate':
            t = list(t)
            t[1] = 'V'
            tags[idx] = tuple(t)
    tags = list(map(lambda x: [x[0], get_wordnet_pos(x[1])], tags))

    words = [lm.lemmatize(w[0], w[1]) if w[1] in tag else w[1] for w in tags]

    return words
