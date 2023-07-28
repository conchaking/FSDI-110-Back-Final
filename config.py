import pymongo
import certifi

con_str = "mongodb+srv://adamyoung_sdgku:Meaningless@cluster0.km9to5v.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("juicestore")