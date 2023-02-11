import pymongo

class DbMongo:
    
    @staticmethod
    def getDB():
        user = 'admin'
        password = 'laureate123'
        cluster = 'cluster0.cgn4a6o.mongodb.net'
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )
 
        client = pymongo.MongoClient(uri)
        db = client['unah']

        return db
