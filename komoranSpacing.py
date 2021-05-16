import json
import sys
import os
import urllib.request
import config
from konlpy.tag import Komoran

client_id = config.id # 개발자센터에서 발급받은 Client ID 값
client_secret = config.pw # 개발자센터에서 발급받은 Client Secret 값

encText = urllib.parse.quote("The current fire house installed within the building used by South Korea’s agency for managing the industrial zone will move to the newly built three-story building, the official said.")
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

komoran = Komoran()
space = ['JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JC', 'JX', 'EP', 'EF', 'EC', 'ETN', 'ETM', 'XSN', 'XSV', 'XSA', 'SF', 'SP', 'VCP', 'VCN'] #띄어쓰기를 하지 않는 품사들을 저장한 리스트

if(rescode==200):
    response_body = response.read()
    my_response_body = response_body.decode('utf-8')
    my_response_body_dict = json.loads(my_response_body)
    x = komoran.pos(my_response_body_dict['message']['result']['translatedText'])
    z = list(map(list, x))

    list = []
    #각 낱말을 리스트에 합성하여 문장으로 만들어준다.
    for i in range (len(z)):
        list.append(z[i][0])

        if (i == len(z) - 1):
            break
        else:
            #조사와 연결어미 등 띄어쓰기를 하지 않는 품사들의 정보를 통해 띄어쓰기 처리를 해준다.
            if (z[i + 1][1] in space):
                continue
            else:
                list.append(" ")

    print("".join(list)) #재합성한 하나의 문장 출력

else:
    print("Error Code:" + rescode)