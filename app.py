import os
import re
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList, Item
from db import db
from resources.store import Store,StoreList

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'uri','sqlite:///data.db'
app.config['SQALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'jose'
api=Api(app)



jwt = JWT(app,authenticate,identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':

    app.run(port=5000, debug=True)
