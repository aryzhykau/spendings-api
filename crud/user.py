from mongodb.client import mongo, mongo_connection


@mongo_connection
def new_user(user_id, name):
    new_user = mongo.db.users.insert_one({'tg_id': user_id, 'name': name, 'wallets': []})
    return new_user


@mongo_connection
def get_name(user_id):
    return mongo.db.users.find_one({'tg_id': user_id})['name']


@mongo_connection
def check_user(user_id):
    return mongo.db.users.find_one({'tg_id': user_id})
