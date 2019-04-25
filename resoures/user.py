import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required


class UserRegister(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='This Field can not be null')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='This Field can not be null')

        data = parser.parse_args()

        if UserModel.find_by_username(username=data['username']):
            return {"message": "User already exists"}, 400
        else:
            user = UserModel(data['username'], data['password'])
            user.save_to_db()
            return {"message": "User Created"}, 201


'''  connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            insert_query = 'insert into users values(NULL, ?, ?)'
            cursor.execute(insert_query, (data['username'], data['password']))
            connection.commit()
            connection.close()'''

