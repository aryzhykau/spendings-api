from app.mongodb.client import mongo, mongo_connection
from bson import ObjectId


@mongo_connection
def new_wallet(user_id, wallet_name):
    new_wallet = {
        'owner_id': user_id,
        'name': wallet_name,
        'balance': 0
    }
    return mongo.db.wallets.insert_one(new_wallet)


@mongo_connection
def check_wallet(user_id, wallet_name):
    return mongo.db.wallets.find_one({'owner_id': user_id, 'name': wallet_name})


@mongo_connection
def get_balance(user_id, wallet_name):
    wallet = mongo.db.wallets.find_one({'owner_id': user_id, '_id': ObjectId(wallet_name)}, {'_id': 0,'balance': 1, 'name': 1})
    result = {
        'balance': wallet['balance'],
        'name': wallet['name']
    }
    return result


@mongo_connection
def remove_wallet(user_id, wallet_name):
    if mongo.db.wallets.find_one({"owner_id": user_id, "_id": ObjectId(wallet_name)}):
        mongo.db.wallets.delete_one({"owner_id": user_id, "_id": ObjectId(wallet_name)})


@mongo_connection
def get_all_wallets_names(user_id):
    wallets = mongo.db.wallets.find({"owner_id": user_id}, {'_id': 1, 'name': 1})
    result = []
    for wallet in wallets:
        result.append({'_id': wallet['_id'],'name': wallet['name']})
    return result
