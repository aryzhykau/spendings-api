from app.mongodb.client import mongo, mongo_connection

@mongo_connection
def create_user(telegram_id, name, base_categories):
    return mongo.db.users.insertOne(
        {
            '_id': telegram_id,
            'spendings': [],
            'categories': base_categories

        }
    )


@mongo_connection
def create_first_wallet(telegram_id, name):
    return mongo.db.wallets.insertOne(
        {
            'owner_id': telegram_id,
            'balance': 0,
            'name': name
        }
    )




