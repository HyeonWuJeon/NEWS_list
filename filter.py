# 3번 : 데이터 정제하기 데이터 끝처리완료.

import subprocess
def filter():

    kbs = open('kbs/kbs.json','r',encoding='utf-8')
    con = kbs.read()
    result = list(con)
    result[-2] =""
    final = "".join(result)

    sbs = open('sbs/sbs.json','r',encoding='utf-8')
    don = sbs.read()
    result = list(don)
    result[-2] =""
    final2 = "".join(result)
    mbc = open('mbc/mbc.json','r',encoding='utf-8')
    mbc = mbc.read()
    result = list(mbc)
    result[-2] =""
    final3 = "".join(result)

    kbs = open('kbs/kbs.json','w',encoding='utf-8')
    sbs = open('sbs/sbs.json','w',encoding='utf-8')
    mbc = open('mbc/mbc.json','w',encoding='utf-8')
    kbs.write(final)
    kbs.write(']}')
    sbs.write(final2)
    sbs.write(']}')
    mbc.write(final3)
    mbc.write(']}')
def main():
    filter()
    print("----------데이터 정제 완료----------")
    # subprocess.call(['python','interlock.py'])

if __name__=="__main__":
    main()
