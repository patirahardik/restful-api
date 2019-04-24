from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is None:
            return {'message': 'Store doesn\'t exist'}, 404
        else:
            return StoreModel.find_by_name(name=name).json()

    def post(self, name):
        if StoreModel.find_by_name(name=name) is not None:
            return {'message': 'Store already exists'}, 400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
                return store.json(), 201
            except:
                return {'message': "Server error while inserting data to database"}, 500

    def delete(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is None:
            return {'message': 'Store doesn\'t exist'}, 404
        else:
            store.delete_from_db()
            return {'message': 'Store deleted'}



class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
