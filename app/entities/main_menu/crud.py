from app.mongodb.client import mongo, mongo_connection

@mongo_connection
def create_user(telegram_id, name, base_categories):
    return mongo.db.users.insert_one(
        {
            '_id': telegram_id,
            'name': name,
            'categories': base_categories

        }
    )

@mongo_connection
def check_user(telegram_id):
    return mongo.db.users.find_one({'_id': telegram_id})




@mongo_connection
def create_first_wallet(telegram_id, name):
    return mongo.db.wallets.insert_one(
        {
            'owner_id': telegram_id,
            'balance': 0,
            'name': name
        }
    )




