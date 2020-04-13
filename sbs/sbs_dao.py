#sbs에
import pymysql
import json

import sys
import io
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='news', charset='utf8')

    return conn


# json 타입의 파일을 읽어온다.
# 파일의 딕셔너리별 키값을 빼온다.
# 쿼리문을 작성하여 저장하고싶은 데이터베이스를 불러온다.
# json 타입의 딕셔너리 쌍과 쿼리문의 쌍을 맞춰서 데이터를 넣어준다
# for문을 사용한다.

# ------------sbs----------------
# 파일명만 계속 바꿔주기

f =  open("sbs/sbs.json",'r',encoding ='utf8')
sbs = f.read()
# print(type(sbs)) #str타입
json_data = json.loads(sbs) #json파일을 읽어온다dict타입
# print(type(json_data))
#\xa0과같은 2byte의 스트링을 제거해준다.
TT ="" #title 데이터가 들어갈 변수
OO ="" #origninallink
LL ="" #link
DD ="" #description
PP ="" #pubdata

# -------------------제목------------------
for i in range(len(json_data['items'])): # 데이터갯수만큼 for문처리

    sbs1 = json_data['items'][i]["title"] #이중 리스트 처리 [[]]
    TT+=sbs1+'__' #title을 TT에 담는다 '__'데이터를 split를 이용하여 리스트로 만들어 주기위해서 사용.
    sbs_title = TT.split("__") #string -> list

# 빈공간 없애주기
if sbs_title[0] ==" ":
    sbs_title.pop(0)
elif sbs_title[-1]==" ":
    sbs_title.pop(-1)
#

#------------------기사링크------------------
for i in range(len(json_data['items'])): # 길이 만큼 돌린다
     sbs2 = json_data['items'][i]["originallink"] + '__' #데이터구분
     OO+=sbs2
sbs_originallink = OO.split("__") #string -> list

sbs_originallink.pop() # 마지막 빈칸 값 제거

#-------------------네이버 링크------------------
for i in range(len(json_data['items'])):
     sbs3 = json_data['items'][i]["link"] + '__'
     LL+=sbs3
sbs_link = LL.split("__")
sbs_link.pop()
# chosun_link[i]

#-------------------본문------------------
for i in range(len(json_data['items'])):
     sbs4 = json_data['items'][i]["description"] + '__'
     DD+=sbs4
sbs_description = DD.split('__')
sbs_description.pop()
# chosun_description[2])

for i in range(len(json_data['items'])):
     sbs5 = json_data['items'][i]["pubDate"] + '__'
     PP+=sbs5
sbs_pubdate = PP.split('__')
sbs_pubdate.pop()
# chosun_pubdate


def add_newsdata(title, link, originallink, description1, pubDate) :

    # 쿼리문 값을 넣어준다
    sql = '''insert into sbs
    (title, link, originallink, description1, pubDate)
    values(%s, %s, %s, %s, %s)'''

    # 데이터 베이스 접속

    conn = get_connection()
    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (title, link, originallink, description1, pubDate))
    conn.commit()


    # 방금 저장한 뉴스 정보 가져온다.
    sql2 = 'select * from sbs'
    cursor.execute(sql2)
    result = cursor.fetchone()
    idx = result[0]

    # 접속 종료
    conn.close()

    return idx
#-------------- 저장된 모든 기사를 가져오는함수----------------
def get_news_list(title) :
        # 데이터베이스 접속
    conn = get_connection()
        # 쿼리문
    sql = '''select news_idx,title, originallink, description1, pubDate
                 from sbs'''# SBS에서 데이터를 가져온다

        # if stu_name != None and len(stu_name) > 0 :     # 검색어가 있을 경우
        #     sql += ' title like %'


    # 쿼리문 실행
    cursor = conn.cursor()

    # excute는 해당쿼리를 실행시키게 함.
    #TITLE를 계속해서 실행
    if title != None and len(title) > 0 :
        cursor.execute(sql, (f'%{title}%'))
    else :
        cursor.execute(sql)

    # 결과를 가져온다.
    result = cursor.fetchall()
    # 데이터를 추출한다.
    temp_list = []
    for row in result :
        temp_dic = {}
        temp_dic['news_idx'] = row[0]
        temp_dic['title'] = row[1]
        temp_dic['originallink'] = row[2]
        temp_dic['description1'] = row[3]
        temp_dic['pubDate'] = row[4]
        temp_list.append(temp_dic) #DICT타입으로 데이터 실행
    conn.close()
    return temp_list


    # # 기사 한개의 정보를 가져오는 함수
def get_news_info(news_idx) :
        # 쿼리문
    sql = '''select news_idx, description1, link
             from sbs
             where news_idx = %s'''
    # 접속
    conn = get_connection()
    # 쿼리 실행
    cursor = conn.cursor()
    # 해당데이터 db에서 가져오기
    cursor.execute(sql, (news_idx))
    result = cursor.fetchone()
    # 데이터 추출
    result_dic = {}
    result_dic['news_idx'] = news_idx #news_idx
    result_dic['news_description1'] = result[1] # description1
    result_dic['news_link'] = result[2] #link
    conn.close()
    return result_dic


# def main():
#     for k in range(len(json_data['items'])):
#         result = add_newsdata(sbs_title[k], sbs_link[k], sbs_originallink[k], sbs_description[k], sbs_pubdate[k])
#     return result
# if __name__=='__main__':
#     main()
# print('에스비에스 저장완료')
