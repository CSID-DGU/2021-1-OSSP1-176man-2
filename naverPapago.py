#encoding=utf-8
import json
import sys
import os
import urllib.request
import config
from konlpy.tag import Komoran

client_id = config.API_ID  # 개발자센터에서 발급받은 Client ID 값
client_secret = config.API_SECRET  # 개발자센터에서 발급받은 Client Secret 값


def translate(inputSentence):
    encText = urllib.parse.quote(inputSentence)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    jsonObject = json.loads(response_body.decode('utf-8'))
    korText = jsonObject.get("message").get("result").get("translatedText")
    print(korText)
    return korText

    # komoran = Komoran()

    # return [komoran.morphs(korText), komoran.pos(korText)]

if __name__ == '__main__':
    str1 = input()
    print(translate(str1))
