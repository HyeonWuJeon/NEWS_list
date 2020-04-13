#2번실행파일. 정제되지않은 API를 각 방송사 JSON 필드에 공급
#방송사 별 필터 기능.
#방송사 별로 데이터를 삽입해준다. 아직 정제하기 전이다
import json
import subprocess

with open("public API/news_korea.json", 'r', encoding="utf8") as f:
    contents = f.read()
    final = contents.replace("'", "")  # 작은따옴표 아예없애버리기
    #print(type(final))
    json_data = json.loads(final)  # 제대로된 json데이터
    # print(json_data['lastBuildDate'])
#

    # json파일로 만들기위해 윗부분 json형식을 끌어온다.
with open("jseting.json", 'r', encoding ="utf8") as ex: #json파일로 세팅해준다.
    seting = ex.read()
#     seting_set = seting.replace("'","")
#     seting = json.loads(seting_set)
#
#     seting['lastBuildDate'] = json_data['lastBuildDate']
#     seting['total'] = json_data['total']
#     seting['start'] = json_data['start']
#     seting['display'] = json_data['display']
# # # #
def data_input():
    #신문사별로 json파일 생성 및 셋팅

    kbs = open("kbs/kbs.json", 'w', encoding="utf8")
    mbc = open("mbc/mbc.json", 'w', encoding="utf8")
    sbs = open("sbs/sbs.json", 'w', encoding="utf8")


    #
    # json.dump(seting, kbs)
    # json.dump(seting, sbs)
    # json.dump(seting, mbc)

    kbs.write(seting)
    mbc.write(seting)
    sbs.write(seting)
    ex.close()
    kbs.close()
    mbc.close()
    sbs.close()

# 자유한국당
# kbs
def kbs_add_data():

    kbs = open("kbs/kbs.json", 'a', encoding="utf8")
    kbs.write('"items": [')

    #dsiplay = 100;
    for i in range(0,100):
        if 'kbs' or 'hkbs' in json_data['items'][i]['originallink']:
            result = str(json_data['items'][i])
            final = result.replace("'",'"').replace('\\x',' ').replace('&quot',' ').replace('<b>','').replace('</b>','').replace(';','')
            kbs.write(final) #바꾼데이터 삽입
            kbs.write(',\n') # pop()로 쉼표를 제거해도된다.(FILTER()함수)


#sb
def sbs_add_data():
    sbs = open("sbs/sbs.json", 'a', encoding="utf8")
    sbs.write('"items": [')
    #dsiplay = 100;
    for i in range(0,100):
        if 'ohmynews' in json_data['items'][i]['originallink']:
            result = str(json_data['items'][i])
            final = result.replace("'",'"').replace('\\x',' ').replace('&quot',' ').replace('<b>','').replace('</b>','').replace(';','')
            sbs.write(final)
            sbs.write(',\n')

#mbc
def mbc_add_data():
    mbc = open("mbc/mbc.json", 'a', encoding="utf8")
    mbc.write('"items": [')
    #dsiplay = 100;
    for i in range(0,100):
        if 'mbc'or'imbc' in json_data['items'][i]['originallink']:
            result = str(json_data['items'][i])
            final = result.replace("'",'"').replace('\\x',' ').replace('&quot',' ').replace('<b>','').replace('</b>','').replace(';','')
            mbc.write(final)
            mbc.write(',\n')
def main():
    data_input()
    mbc_add_data()
    sbs_add_data()
    kbs_add_data()
    print('---------- 자유한국당 데이터 삽입 완료----------')
    subprocess.run(['python', 'input_data_minju.py'])
if __name__ =="__main__":
    main()
