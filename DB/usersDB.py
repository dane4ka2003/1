import sqlite3


class UsersDataBase(object):

    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cur = self.db.cursor()


    def add_user(self, id, username):
        self.cur.execute('INSERT INTO users(id, username) VALUSES (?, ?);', (id, username))
        self.db.commit()


    def give_subscription_to_user(self, interval):
        self.cur.execute()





db = UsersDataBase('users_db.sqbpro')