from mongodb.client import mongo, mongo_connection
from datetime import date


@mongo_connection
def add_balance(user_id, wallet_name, amount):
    update_query = {"$set":{"wallets.$.balance": amount}}
    mongo.db.users.update_one({'tg_id': user_id, "wallets.name": wallet_name}, update_query)

@mongo_connection
def add_spending(user_id, wallet_name, amount, category):
    user_wallet = mongo.db.users.find_one({'tg_id': user_id, 'wallets.name': wallet_name}, {'wallets.$': 1})
    user_balance = user_wallet['wallets'][0]['balance']
    if amount <= 0:
        return {'error': 'Сумма трат меньше 0'}
    if amount > user_balance or user_balance <= 0:
        return {'error': 'В кошельке закончились средства('}
    else:
        update_query = {
            "$push": {
                'spendings': {
                    'category': category,
                    'amount': amount,
                    'wallet': wallet_name,
                    'date': date.today()
                }
            }
        }
        user_balance = user_balance - amount
        mongo.db.users.update_one({'tg_id': user_id}, update_query)
        mongo.db.users.update_one(
            {'tg_id': user_id, 'wallets.name': wallet_name},
            {'$set': {'wallets.$.balance': user_balance}}
        )

@mongo_connection
def get_all_spendings(user_id):
    user = {'tg_id': user_id}
    data = mongo.db.users.find_one(user)
    return data['spendings']


@mongo_connection
def get_spendings_by_wallet(user_id, wallet_name):
    user = {'tg_id': user_id}
    filter = {
        'tg_id': user_id,
        'spendings': {
            '$filter': {
                'input': '$spendings',
                'as': 'element',
                'cond': {
                    '$eq': ['$$spending.wallet', wallet_name]
                }
            }
        }
    }
    result = mongo.db.users.aggregate([{'$match': {'tg_id': user_id}}, {'$project': filter}])
    return result
