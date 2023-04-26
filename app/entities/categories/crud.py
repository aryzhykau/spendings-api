from app.mongodb.client import mongo, mongo_connection

@mongo_connection
def create_category(id, name, emoji):
    mongo.db.categories.insert_one(
        {
            'name': name,
            'emoji': emoji
        }
    )
    category_id = mongo.db.categories.find_one({'name': name}, {'_id': 1})
    print(category_id)
    mongo.db.users.update_one({'_id': id}, {'$push': {'categories': category_id['_id']}})

@mongo_connection
def check_category(name):
    if mongo.db.categories.find_one({'name': name}):
        return True
    else:
        return False


@mongo_connection
def get_all_user_categories(id):
    categories_ids = mongo.db.users.find_one({'_id': id}, {'_id': 1, 'categories': 1})['categories']
    categories = mongo.db.categories.find({'_id': {'$in': categories_ids}})
    result = []
    for category in categories:
        result.append({'_id':category['_id'], 'name': category['name'], 'emoji': category['emoji']})
    print(result)
    return result







