
import pymysql
# 데이터 베이스에 접속하는 함수
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='news', charset='utf8', port='')

    return conn

# Birng sbs news list
def get_news_list_sbs(title) :
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

# bring kbs news list
def get_news_list_kbs(title) :
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
        temp_list.append(temp_dic) #DICT타입으로 데이터 실행
    conn.close()
    return temp_list
# 학생 정보를 저장한다.

#bring mbc news list
def get_news_list_mbc(title) :
    # contact database
    conn = get_connection()
    # query string
    sql = '''select news_idx, title, originallink, description1, pubDate
             from mbc'''# bring data in mbc

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
def get_news_info_sbs(news_idx) :
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

def get_news_info_mbc(news_idx) :
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

def get_news_info_kbs(news_idx) :
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

# 유저 댓글정보 저장.
def add_comment(user_name, user_pwd, user_comment) :
    # 쿼리문
    sql = '''insert into user_comment
             (user_name, user_pwd, user_comment)
             values (%s, %d, %s)'''
    # 데이터 베이스 접속
    conn = get_connection()

    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (user_name, user_pwd, user_comment)) #추출한 값 insert
    conn.commit()

    # 방금 저장한 댓글 사용자의 이름를 가져온다.
    sql2 = 'select max(user_idx) from user_comment'
    cursor.execute(sql2)
    result = cursor.fetchone()
    idx = result[0]

    # 접속 종료
    conn.close()

    return idx


#get_news_info()
# if __name__=='__main__':
#     # get_connection()
#     result = add_comment(user_name, user_pwd, user_comment)
#     print(result)
