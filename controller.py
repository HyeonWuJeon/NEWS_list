# database파일 손보기.
#마지막 실행파일
from flask import Flask, render_template, request, Blueprint,session,redirect,url_for
import database as db
import sbs.sbs_dao as sbdb
import kbs.kbs_dao as kbdb
import mbc.mbc_dao as mbdb
import subprocess
from user import user_dao

app = Flask(__name__, template_folder='html') #부모 폴더를 탬플릿폴더에넣어둔다.

app.secret_key = 'selkjfoiwejfoiwjfoijiofj'


@app.route('/')

def front():

    html = render_template('include/top_menu.html') #render_temlplate 으로 html폴더를 불러올수 있다.

    return html



@app.route('/sbs')
def title_list_sbs() :
    # 검색어를 추출한다.
    # get 방식으로 파라미터 데이터 추출
    title = request.args.get('title')
    # 뉴스 정보 를 가져온다
    title_list = sbdb.get_news_list(title) # 해당함수에서 값을 가져온다

    # 클라이언트 브라우저에게 전달할 문자열을 html파일을 읽어와서 생성한다.
    #1 탬플릿의이름.html
    #2 탬플릿에 보여줄 변수를 키워드 인자로 넘겨준다
    html = render_template('sbs.html', data_list=title_list) #변수명 마음대로 지정해도된다. html에서도 똑같이 쓰는거 잊지말기
    return html

@app.route('/mbc')
def title_list_mbc() :
    # 검색어를 추출한다.
    # get 방식으로 파라미터 데이터 추출
    title = request.args.get('title')
    print(title)
    # 뉴스 정보 를 가져온다
    title_list = mbdb.get_news_list(title) # 해당함수에서 값을 가져온다

    # 클라이언트 브라우저에게 전달할 문자열을 html파일을 읽어와서 생성한다.
    #1 탬플릿의이름.html
    #2 탬플릿에 보여줄 변수를 키워드 인자로 넘겨준다
    html = render_template('mbc.html', data_list=title_list) #변수명 마음대로 지정해도된다. html에서도 똑같이 쓰는거 잊지말기
    return html

@app.route('/kbs')
def title_list_kbs() :
    # 검색어를 추출한다.
    # get 방식으로 파라미터 데이터 추출
    title = request.args.get('title')
    print(title)
    # 뉴스 정보 를 가져온다
    title_list = kbdb.get_news_list(title) # 해당함수에서 값을 가져온다

    # 클라이언트 브라우저에게 전달할 문자열을 html파일을 읽어와서 생성한다.
    #1 탬플릿의이름.html
    #2 탬플릿에 보여줄 변수를 키워드 인자로 넘겨준다
    html = render_template('kbs.html', data_list=title_list) #변수명 마음대로 지정해도된다. html에서도 똑같이 쓰는거 잊지말기
    return html

#sbs기사 자세한정보
@app.route('/news_info_sbs', methods=['get', 'post'])
def news_info_sbs() :
    # 파라미터 데이터 추출
    news_idx = request.args.get('news_idx')
    # 추출한 데이터정보 삽입
    result_dic = db.get_news_info_sbs(news_idx)

    html = render_template('info_html/news_info_sbs.html', data_dic=result_dic)
    return html

#kbs 자세한정보
@app.route('/news_info_kbs', methods=['get', 'post'])
def news_info_kbs() :
    # 파라미터 데이터 추출
    news_idx = request.args.get('news_idx')
    # 추출한 데이터정보 삽입
    result_dic = db.get_news_info_kbs(news_idx)

    html = render_template('info_html/news_info_kbs.html', data_dic=result_dic)
    return html

#mbc기사 자세한정보
@app.route('/news_info_mbc', methods=['get', 'post'])
def news_info_mbc() :
    # 파라미터 데이터 추출
    # get방식으로 요청정보넘기기
    news_idx = request.args.get('news_idx')

    # 추출한 데이터정보 삽입
    # 넘어간 정보를 데이터에 삽입한다.
    result_dic = db.get_news_info_mbc(news_idx)

    # 데이터키워드인자를 탬플릿 폴더에 전달한다.
    html = render_template('info_html/news_info_mbc.html', data_dic=result_dic)
    return html
   # 파라미터 데이터 추출

# 댓글 정보
# @app.route('/add_news', methods=['get','post'])
# def add_news() :
#     html = render_template('add_news.html')
#     return html
#


@app.route('/add_news_pro', methods=['get','post'])
def add_news_pro() :
    # 해당사이트에 저장된내용 파라미터 데이터 추출한다.
    user_name = request.form['user_name']
    user_pwd = request.form['user_pwd']
    user_comment = request.form['user_comment']

    # print(f'{stu_name} {stu_age} {stu_addr}')
    # 저장한다.
    # idx에 해당 값저장
    idx = db.add_comment(user_name, user_pwd, user_comment)


    result_dic = { 'user_idx' : idx}

    html = render_template('add_news_pro.html', data_dic=result_dic)
    return html



#  User Controller



@app.route('/user/user_login')
def user_login() :
    html = render_template('user/user_login.html')
    return html


@app.route('/user/user_join')
def user_join() :
    html = render_template('user/user_join.html')
    return html

@app.route('/user/user_modify')
def user_modify() :
    html = render_template('user/user_modify.html')
    return html


@app.route('/user_join_pro', methods=['post'])
def user_join_pro() :
    # 파라미터 데이터 추출
    user_name = request.form['user_name']
    user_id = request.form['user_id']
    user_pw = request.form['user_pw']

    # print(user_name)
    # print(user_id)
    # print(user_pw)
    # print('저장완료')

    user_dao.add_user(user_name, user_id, user_pw)

    return 'OK'


@app.route('/check_user_id', methods=['post'])
def check_user_id() :
        # 아이디 추출
    user_id = request.form['user_id']
    # 확인
    result = user_dao.check_user_id(user_id)

    return result



# 로그인 처리
@app.route('/user_login_pro', methods=['post'])
def user_login_pro() :
    # 파라미터 추출
    user_id = request.form['user_id']
    user_pw = request.form['user_pw']
    # 확인한다.
    result = user_dao.check_login(user_id, user_pw)

    if result == 'NO' :
        return 'NO'
    else :
        session['login'] = 'YES'
        session['user_idx'] = result
        return 'YES'


@app.route('/logout')
def logout():
    session.pop('user_idx', None)
    session.pop('login', None)
    return redirect('/')


print('********************************웹 애플리케이션 실행********************************')
app.run(host='0.0.0.0', port=80)
