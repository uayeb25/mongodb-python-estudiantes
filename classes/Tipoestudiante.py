from classes.DbMongo import DbMongo
class Tipoestudiante:

    def __init__(self, tipo, id = ""):
        self.tipo = tipo
        self.__id = id
        self.__collection = "tipo_estudiante"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_one(db, id):
        collection = db["tipo_estudiante"]
        filterToUse = { '_id' : id }
        result = collection.find_one(filterToUse)

        return Tipoestudiante( result["tipo"] , result["_id"] )


    @staticmethod
    def get_list(db):
        collection = db["tipo_estudiante"]
        tipos = collection.find()

        list_tipo_estudiantes = []
        for e in tipos:
            temp_tipo = Tipoestudiante(
                e["tipo"]
                , e["_id"] 
            )

            list_tipo_estudiantes.append(temp_tipo)
        return list_tipo_estudiantes
    
    @staticmethod
    def get_dict(db):
        collection = db["tipo_estudiante"]
        tipos = collection.find()

        dict_tipo_estudiantes = {}
        for e in tipos:
            dict_tipo_estudiantes[e["tipo"]] = e["_id"] 

        return dict_tipo_estudiantes
    
    @staticmethod
    def delete_all(db):
        lista_e = Tipoestudiante.get_list(db)
        for e in lista_e:
            e.delete(db)
        



        