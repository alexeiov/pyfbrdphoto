from getphoto import config
import fdb


def db_connect(db_path):
    con = fdb.connect(dsn=db_path, user=config.USERNAME, password=config.PASSWD,
                      charset='win1251')
    cur = con.cursor()
    return con, cur


if __name__ == 'main':
    db_connect()
