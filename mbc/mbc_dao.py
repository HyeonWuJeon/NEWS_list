#데이터 베이스에 값을 저장하는 함수
import pymysql
import json
import flask
import sqlite3
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='news', charset='utf8')
    return conn
def filter():
    with open('mbc/mbc.json','r',encoding ='utf8') as f:
        mbc= f.read()
        mbc_result = mbc.split("\\")
        mbc_final = "".join(mbc_result)
        f.close()
    return mbc_final

# ------------mbc----------------
result = filter()

with open('mbc/mbc.json','w',encoding='utf8') as f:
    f.write(result)
    json_data=json.loads(result)
TT ="" #title 데이터가 들어갈 변수
OO ="" #origninallink
LL ="" #link
DD ="" #description
PP ="" #pubdata

#-------------------제목
for i in range(len(json_data['items'])): # 길이 만큼 돌린다
    mbc1 = json_data['items'][i]["title"] #이중 리스트 처리 [[]]
    TT+=mbc1+'__'
    mbc_title = TT.split("__") #chosun
if mbc_title[0] == " ":
    mbc_title.pop(0)
elif mbc_title[-1]== "":
    mbc_title.pop(-1)

#
#
#------------------기사링크
for i in range(len(json_data['items'])): # 길이 만큼 돌린다
     mbc2 = json_data['items'][i]["originallink"] + '__'
     OO+=mbc2
mbc_originallink = OO.split("__") #string->list
mbc_originallink.pop() # 마지막 빈칸 값 혹은 쉼표 제거

#-------------------네이버 링크
for i in range(len(json_data['items'])):
     mbc3 = json_data['items'][i]["link"] + '__'
     LL+=mbc3
mbc_link = LL.split("__") #string -> list
mbc_link.pop() #마지막 빈칸 값 혹은 쉼표 제거

#-------------------본문
for i in range(len(json_data['items'])):
     mbc4 = json_data['items'][i]["description"] + '__'
     DD+=mbc4
mbc_description = DD.split('__') #string->list
mbc_description.pop() #마지막 빈칸 값 혹은 쉼표제거



#-------------------날짜
for i in range(len(json_data['items'])):
     mbc5 = json_data['items'][i]["pubDate"] + '__'
     PP+=mbc5
mbc_pubdate = PP.split('__') #string->list
mbc_pubdate.pop() #마지막 빈칸 값 혹은 쉼표제거



def add_newsdata(title, link, originallink, description1, pubDate) :

    conn = get_connection()
    # 데이터 베이스 접속
    # 쿼리문
    sql = '''insert into mbc
    (title, link, originallink, description1, pubDate)
    values(%s, %s, %s, %s, %s)'''

    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (title, link, originallink, description1, pubDate))
    conn.commit()

#---------------방금 저장한 뉴스데이터 가져오기---------------

    sql2 = 'select * from mbc'
    cursor.execute(sql2)
    result = cursor.fetchone()
    idx = result[0]

    # 접속 종료
    conn.close()
#------------------------------------------------------------

#-------------- 저장된 모든 기사를 가져오는함수----------------
def get_news_list(title) :
        # 데이터베이스 접속
    conn = get_connection()
        # 쿼리문
    sql = '''select news_idx,title, originallink, description1, pubDate
                 from mbc'''# SBS에서 데이터를 가져온다

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
             from mbc
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
#
# def main():
#     for k in range(len(json_data['items'])):
#         result = add_newsdata(mbc_title[k], mbc_link[k], mbc_originallink[k], mbc_description[k], mbc_pubdate[k])
#     return result
# # all_news_list = get_news_info(1)
# # printf("all_news_list") #현재까지 모두저장된 뉴스의 리스트
# if __name__=='__main__':
#      main()
#      print('엠비씨 저장완료')
