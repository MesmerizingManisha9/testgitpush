import pymongo
client = pymongo.MongoClient("mongodb+srv://manisha6:manisha999@cluster0.y49ybvh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "Manisha" ,`
    "email" : "manisha@gmail.com" ,
    "surname" : " Sharma"
}

db1 = client['mongotest']
coll= db1['test']
coll.insert_one(d)

