import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    ''' connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        find_query = "select * from users where username = ?"
        result = cursor.execute(find_query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user'''

    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter_by(id=_id).first()


'''   connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        find_query = "select * from users where id = ?"
        result = cursor.execute(find_query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user'''
