import sqlite3


class UsersDataBase:

    def __init__(self):
        self.db = sqlite3.connect('admin.db')
        self.cur = self.db.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            userid INTEGER,
                            username TEXT,
                            subscription TEXT)
                            """)
        self.db.commit()


    def add_user(self, userid, username):
        self.cur.execute('INSERT INTO users(userid, username, subscription) VALUES (?, ?, "-");', (userid, username))
        self.db.commit()


    def get_userids(self):
        userids = self.cur.execute('SELECT userid FROM users').fetchall()
        return userids


    def give_subscription_to_user(self, interval):
        self.cur.execute()


userdb = UsersDataBase()
userdb.add_user(1234, 'dan')
print(userdb.get_userids())




