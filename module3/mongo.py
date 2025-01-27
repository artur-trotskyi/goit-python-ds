####################################### Створення документів #######################################

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://arturtrotskyi:aqswdefr1@cluster0.qtel3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)

####################################### Отримання документів #######################################

from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://arturtrotskyi:aqswdefr1@cluster0.qtel3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

result = db.cats.find_one({"_id": ObjectId("60d24b783733b1ae668d4a77")})
print(result)

####################################

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://arturtrotskyi:aqswdefr1@cluster0.qtel3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)
db = client.book

result = db.cats.find({})
for el in result:
    print(el)

####################################### Оновлення документів #######################################

from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)
db = client.book

db.cats.update_one({"name": "barsik"}, {"$set": {"age": 4}})
result = db.cats.find_one({"name": "barsik"})
print(result)

####################################### Видалення документів #######################################

from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)
db = client.book

db.cats.delete_one({"name": "barsik"})
result = db.cats.find_one({"name": "barsik"})
print(result)
