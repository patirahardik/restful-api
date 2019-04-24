from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemsModel


class ItemList(Resource):
    @jwt_required()
    def get(self):
        items = ItemsModel.query.all()
        return {'items': [x.json() for x in items]}

    '''    connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        retrieve_query = "select name,price from items"
        result = cursor.execute(retrieve_query)
        item_list = []
        for row in result:
            item_list.append(ItemsModel(*row).json())
        return {'items': item_list}
'''


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field can not be empty"
                        )
    parser.add_argument("store_id",
                        type=int,
                        required=True,
                        help="This field can not be empty"
                        )

    def get(self, name):
        item = ItemsModel.find_by_name(name)
        if item:
            return item.json(), 200
        else:
            return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemsModel.find_by_name(name) is not None:
            return {"message": "An item name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        item = ItemsModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error while inserting an item.'}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemsModel.find_by_name(name)
        if item is None:
            return {"message": "Item Not Found"}, 400
        else:
            try:
                item.delete_from_db()
            except:
                {'message': 'An error while deleting an item.'}, 500

            return {'message': "Item deleted."}

    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemsModel.find_by_name(name)

        if item is None:
            item = ItemsModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()
        return item.json(), 200
