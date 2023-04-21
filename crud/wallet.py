from mongodb.client import mongo, mongo_connection


@mongo_connection
def new_wallet(user_id, wallet_name):
    update_query = {
        '$push': {
            'wallets': {
                'name': wallet_name,
                'balance': 0
            }}}
    new_wallet = mongo.db.users.update_one({'tg_id': user_id}, update_query)
    return new_wallet


@mongo_connection
def check_wallet(user_id, wallet_name):
    return mongo.db.users.find_one({'tg_id': user_id, 'wallets.name': wallet_name})


@mongo_connection
def get_balance(user_id, wallet_name):
    user = mongo.db.users.find_one({'tg_id': user_id, 'wallets.name': wallet_name}, {'wallets.$': 1})
    balance = user['wallets'][0]['balance']
    return balance


@mongo_connection
def remove_wallet(user_id, wallet_name):
    if mongo.db.users.find_one({"tg_id": user_id,"wallets.name": wallet_name}):
        mongo.db.users.update_one({"tg_id": user_id}, {"$pull": {"wallets": {"name": wallet_name}}})


@mongo_connection
def get_all_wallets(user_id):
    user = mongo.db.users.find_one({'tg_id': user_id})
    return user["wallets"]


@mongo_connection
def get_all_wallets_names(user_id):
    user = mongo.db.users.find_one({'tg_id': user_id})
    print(user)
    wallets = user["wallets"]
    names = []
    for wallet in wallets:
        names.append(wallet["name"])
    return names
