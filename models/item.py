from db import db


class ItemsModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store = db.relationship('StoreModel')
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    ''' connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        find_query = "select name,price from items where name = ?"
        result = cursor.execute(find_query, (name,))
        row = result.fetchone()
        if row:
            item = cls(*row)
        else:
            item = None
        connection.close()
        return item '''

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        ''' connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        insert_query = "insert into items values (NULL,?,?)"
        cursor.execute(insert_query, (self.name, self.price))
        connection.commit()
        connection.close()'''

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        '''connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        delete_query = 'delete from items where name=?'
        cursor.execute(delete_query, (self.name,))
        connection.commit()
        connection.close()'''

    '''def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        delete_query = 'update items set price=? where name=?'
        cursor.execute(delete_query, (self.price, self.name))
        connection.commit()
        connection.close()'''
