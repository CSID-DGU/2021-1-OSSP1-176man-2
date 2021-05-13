import config
from konlpy.tag import Hannanum, Kkma
import os
import sys
import json
import urllib.request
import hgtk

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

client_id = config.API_ID  # 개발자센터에서 발급받은 Client ID 값
client_secret = config.API_SECRET  # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("Nice to meet you")
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()


hannanum = Hannanum()
kkma = Kkma()
#x=hannanum.pos("밥을 먹어서 좋았다.", 22)


if(rescode == 200):
    response_body = response.read()

    my_response_body = response_body.decode('utf-8')
    my_response_body_dict = json.loads(my_response_body)
    # print(my_response_body_dict['message']['result']['translatedText'])
    y = kkma.pos(my_response_body_dict['message']
                 ['result']['translatedText'], 56)
    z = list(map(list, y))
    z[3][0] = "습니다"
    str = ""
    for i in range(4):
        str += (z[i][0])

    after = hgtk.text.compose(str)
    print(after)
else:
    print("Error Code:" + rescode)
