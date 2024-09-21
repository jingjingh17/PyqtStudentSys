import sqlite3
from utils.file_location import get_project_root

class login():
    def __init__(self):
        self.root = get_project_root()
        self.dbPath = self.root + '\\db\\Maindb.db'

        self.conn = sqlite3.connect(self.dbPath)
        
    def check_user(self, username, password):
        cursor = self.conn.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        cursor.close()
        self.conn.close()
        if result:
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    w = login()
    print(w.check_user('admin', '123'))