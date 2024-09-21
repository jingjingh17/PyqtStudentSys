import sqlite3
from utils.file_location import get_project_root

class Auth():
    def __init__(self):
        self.root = get_project_root()
        self.dbPath = self.root + '\\db\\Maindb.db'

        self.conn = sqlite3.connect(self.dbPath)
        
    def check_user_login(self, username, password):
        cursor = self.conn.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        cursor.close()
        self.conn.close()
        if result:
            return True
        else:
            return False
        
    def check_user_register(self, username):
        cursor = self.conn.execute("SELECT * FROM Users WHERE username=?", (username,))
        result = cursor.fetchone()
        if result:
            return False
        else:
            cursor.close()
            self.conn.close()
            return False
        
        
if __name__ == '__main__':
    w = Auth()
    print(w.check_user_login('admin', '123'))