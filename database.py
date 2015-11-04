import pymysql
def explode(command):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='no_name',autocommit=True)
    cur = conn.cursor()
    cur.execute(command)
    for i in cur:
        print(i)
    return cur