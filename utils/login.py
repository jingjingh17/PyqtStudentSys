import sqlite3
import time
from utils.file_location import get_project_root

class Auth():
    def __init__(self):
        self.root = get_project_root()
        self.dbPath = self.root + '\\db\\Maindb.db'

        self.conn = sqlite3.connect(self.dbPath)
        
    def check_user_login(self, username, password):
        cursor = self.conn.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        
        if result:
            '登录成功后,返回ID及角色信息'
            userId = result[0]
            role = result[3]
            return True,userId,role
        else:
            return False,None,None
        
    def check_user_register(self, username,password):
        cursor = self.conn.execute("SELECT * FROM Users WHERE username=?", (username,))
        userExit = cursor.fetchone()
        if not userExit:
            self.conn.execute("INSERT INTO Users (username, password,role,created_at) VALUES (?, ?,?,?)", (username, password,'student',time.strftime('%Y-%m-%d %H:%M:%S')))
            self.conn.commit()
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    w = Auth()
    print(w.check_user_login('admin', '123'))
    print(w.check_user_register('admin'))