import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
 
 
import mysql.connector
 
basedir = os.path.dirname(os.path.abspath(__file__))
 
class DevConfig(Config):
    # Dev Config
    ENV = 'dev'
    DEBUG = True
    TESTING = True

    # Dev Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/mariadb'

    # 데이터베이스 Binds
    SQLALCHEMY_BINDS = {
        'mariadb'    : 'mysql://root:root@127.0.0.1:3306/mariadb',
        'EXPORT'  : 'mysql://root:root@127.0.0.1:3306/EXPORT',
        'WH'      : 'mysql://root:root@127.0.0.1:3306/WH',
        'WH_SLAVE': 'mysql://root:root@127.0.0.1:3306/WH'
    } 
db = {
    'user' : 'root',
    'password' : 'root',
    'host' : 'localhost',
    'port' : '3306',
    'database' : 'mariadb'
}
 
 
mysql_con = None
 
#------------------------------------------------------#
def query_executor(cursor):
    sql = "select * from food"
    cursor.execute(sql,)
#------------------------------------------------------#
 
 
if __name__ == "__main__":
 
    print('test')
    try:
 
        mysql_con = mysql.connector.connect(host='localhost', port='3306', database='mariadb', user='root', password='root')
                                            
        mysql_cursor = mysql_con.cursor(dictionary=True)
 
        query_executor(mysql_cursor)
 
        for row in mysql_cursor:
            print('price is: '+str(row['price']))
        mysql_cursor.close()
 
 
 
    except Exception as e:
        print(e.message)
 
 
    finally:
        if mysql_con is not None:
            mysql_con.close()