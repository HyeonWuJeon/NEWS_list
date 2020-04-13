#1번 실행파일 정제되지 않은 데이터 삽입
import urllib.request
import json
import subprocess
import os
import sys
client_id = "qNIqwuuSolsLVxcLIur1"
client_secret = "K7Yta8iu49"
encText = urllib.parse.quote("한국당")
url = "https://openapi.naver.com/v1/search/news?display=100&query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode("utf8"))

else:
    print("Error Code:" + rescode)
#-----------------------------------------
#news.json
with open('public API/news_korea.json', 'w', encoding="utf8") as f:
    f.write(response_body.decode("utf8"))

client_id = "qNIqwuuSolsLVxcLIur1"
client_secret = "K7Yta8iu49"
encText = urllib.parse.quote("민주당")
url = "https://openapi.naver.com/v1/search/news?display=100&query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode("utf8"))

else:
    print("Error Code:" + rescode)
#-----------------------------------------
#news.json
with open('public API/news_minju.json', 'w', encoding="utf8") as f:
    f.write(response_body.decode("utf8"))

subprocess.run(['python', 'input_data.py'])
