from classes.DbMongo import DbMongo
from classes.Tipoestudiante import Tipoestudiante
class Estudiante:

    def __init__(self, nombre, apellido, telefono, tipo_estudiante ,id = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.tipo_estudiante = tipo_estudiante
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
                , e["tipo_estudiante"]
                , e["_id"] 
            )

            list_estudiantes.append(temp_estudiante)
        return list_estudiantes
    
    @staticmethod
    def delete_all(db):
        lista_e = Estudiante.get_list(db)
        for e in lista_e:
            e.delete(db)

    @staticmethod
    def print_full_report_long_path(db):
        collection = db["estudiante"]

        for e in collection.find():
            r = { 
                "nombre" : e["nombre"]
                , "telefono": e["telefono"] 
                , "tipo": Tipoestudiante.get_one(db, e["tipo_estudiante"] ).tipo
            }
            print(r)

    @staticmethod
    def print_full_report_short_path(db):
        collection = db["estudiante"]

        result = collection.aggregate([
            {
                '$lookup': {
                    'from': "tipo_estudiante"
                    , 'localField': "tipo_estudiante"
                    , "foreignField": "_id"
                    , "as": "te"
                }
            },{
                '$project': {
                    'nombre': 1
                    , 'telefono': 1
                    , 'te.tipo': 1
                }  
            }
        ])

        for d in result:
            print(d)

        



        