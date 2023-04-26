from app.mongodb.client import mongo, mongo_connection
from bson import ObjectId


@mongo_connection
def add_budget(wallet_id, amount):
    wallet = mongo.db.wallets.find_one({'_id': ObjectId(wallet_id)}, {'_id': 1})
    mongo.db.wallets.update_one(wallet, {'$set': {'balance': amount}})
