import pymysql
from operator import itemgetter

connection = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='no_name', autocommit=True, charset='utf8')

def explode(command):
    global connection
    conn = connection.cursor()
    conn.execute(command)
    return conn.fetchall()

try:
    idd=int(explode('SELECT * FROM depending ORDER BY `first` DESC LIMIT 0, 1')[0][0])
except IndexError:
    idd=0

def get_themes():
    global connection
    cur = connection.cursor()
    cur.execute("SELECT * FROM theme")
    return cur


def add_note(record, theme, id_of_previous=None):
    global idd
    idd += 1
    if id_of_previous == None:
        explode('INSERT INTO records (`hex`,`record`,`theme`) VALUES ("{0}","{1}","{2}")'.format(str(idd), str(record),
                                                                                                 str(theme)))
    else:
        explode('INSERT INTO records (`hex`,`record`,`theme`) VALUES ("{0}","{1}","{2}")'.format(str(idd), str(record),
                                                                                                 str(theme)))
        explode('INSERT INTO depending (`first`, `second`, `theme`) VALUES ("{0}","{1}","{2}")'.format(str(idd),
                                                                                                       str(
                                                                                                           id_of_previous),
                                                                                                       str(theme)))


def add_theme(theme):
    explode('INSERT INTO theme (`theme`) VALUES ("{0}")'.format(str(theme)))


def get_note_by_theme(theme):
    global connection
    main = []
    cur = connection.cursor()
    cur.execute("SELECT * FROM records WHERE `theme` = '{0}'".format(str(theme)))
    for item in cur.fetchall():
        main.append(list(item))
    for item in main:
        depend_item = \
        explode('SELECT * FROM depending WHERE `theme` = "{0}" AND `first` = "{1}"'.format(str(theme), str(item[0])))[
            0][1]
        item.append(int(depend_item))
        if depend_item == '-1':
            item[4]=int(item[0])
        else:
            item[3]=""+item[3]
    main.sort(key=itemgetter(4))
    return main

def add_depend(first,second,theme):
    explode('INSERT INTO depending (`first`,`second`,`theme`) VALUES ("{0}","{1}","{2}")'.format(str(first),str(second),str(theme)))

def get_depending_by_id(id):
    global connection
    cur = connection.cursor()
    cur.execute("SELECT * FROM depending WHERE `first` = '{0}'".format(str(id)))
    return cur.fetchall()[0][1]
