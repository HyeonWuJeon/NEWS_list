import pymysql
import json

def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='news', charset='utf8')

    return conn


# json 타입의 파일을 읽어온다.
# 파일의 딕셔너리별 키값을 빼온다.
# 쿼리문을 작성하여 저장하고싶은 데이터베이스를 불러온다.
# json 타입의 딕셔너리 쌍과 쿼리문의 쌍을 맞춰서 데이터를 넣어준다
# for문을 사용한다.

# ------------KBS----------------
# 파일명만 계속 바꿔주기
f =  open('kbs/kbs.json','r',encoding ='utf8')
kbs = f.read()
json_data = json.loads(kbs) #json파일을 읽어온다
TT ="" #title 데이터가 들어갈 변수
OO ="" #origninallink
LL ="" #link
DD ="" #description
PP ="" #pubdata

#-------------------제목
for i in range(len(json_data['items'])): # 길이 만큼 돌린다

     kbs1 = json_data['items'][i]["title"]
     TT+=kbs1+'__'
     kbs_title = TT.split("__")  # chosun
     # 데이터 정제하기

if "[SC<b>리뷰</b>]" in TT:
    kbs_title = TT.split("[SC<b>리뷰</b>]") #해당 문구를 없앤다.
elif "[DA:<b>리뷰</b>]" in TT:
    kbs_title = TT.split("[DA:<b>리뷰</b>]")
# elif "&quot;" in TT:
#     kbs_title = TT.split("&quot;")
if kbs_title[0] == " ":
    kbs_title.pop(0)
elif kbs_title[-1]==" ":
    kbs_title.pop(-1)

#------------------기사링크
for i in range(len(json_data['items'])): # 길이 만큼 돌린다
     kbs2 = json_data['items'][i]["originallink"] + '__'
     OO+=kbs2
kbs_originallink = OO.split("__")
kbs_originallink.pop() # 마지막 빈칸 값 혹은 쉼표 제거


#-------------------네이버 링크
for i in range(len(json_data['items'])):
     kbs3 = json_data['items'][i]["link"] + '__'
     LL+=kbs3
kbs_link = LL.split("__")
kbs_link.pop()
# chosun_link[i]

#-------------------본문
for i in range(len(json_data['items'])):
     kbs5 = json_data['items'][i]["description"] + '__'
     DD+=kbs5
kbs_description = DD.split('__')
kbs_description.pop()
# chosun_description[2])

for i in range(len(json_data['items'])):
     kbs5 = json_data['items'][i]["pubDate"] + '__'
     PP+=kbs5
kbs_pubdate = PP.split('__')
kbs_pubdate.pop()
# chosun_pubdate


def add_newsdata(title, link, originallink, description1, pubDate) :

    conn = get_connection()
    # 쿼리문
    #데이터 삽입
    sql = '''insert into kbs
    (title, link, originallink, description1, pubDate)
    values(%s, %s, %s, %s, %s)'''

    # 데이터 베이스 접속


    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (title, link, originallink, description1, pubDate))
    conn.commit()


    # 방금 저장한 뉴스를 가져온다.
    sql2 = 'select * from kbs'
    cursor.execute(sql2)
    result = cursor.fetchone()
    idx = result[0]

    # 접속 종료
    conn.close()
    #-------------- 저장된 모든 기사를 가져오는함수----------------
def get_news_list(title) :
        # 데이터베이스 접속
    conn = get_connection()
        # 쿼리문
    sql = '''select news_idx,title, originallink, description1, pubDate
                 from kbs'''# SBS에서 데이터를 가져온다

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
        temp_list.append(temp_dic) #DICT타입SS으로 데이터 실행
    conn.close()
    return temp_list


        # # 기사 한개의 정보를 가져오는 함수
def get_news_info(news_idx) :
                # 쿼리문
    sql = '''select news_idx, description1, link
             from kbs
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
#         result = add_newsdata(kbs_title[k], kbs_link[k], kbs_originallink[k], kbs_description[k], kbs_pubdate[k])
#     return result
# if __name__=='__main__':
#      main()
#      print('케이비에스 저장완료')
