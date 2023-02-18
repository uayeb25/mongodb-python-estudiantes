from classes.DbMongo import DbMongo
class Estudiante:

    def __init__(self, nombre, apellido, telefono, id = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__id = id
        self.__collection = "estudiante"

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
    def get_list(db):
        collection = db["estudiante"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiante = Estudiante(
                e["nombre"]
                , e["apellido"]
                , e["telefono"]
                , e["_id"] 
            )

            list_estudiantes.append(temp_estudiante)
        return list_estudiantes
        



        