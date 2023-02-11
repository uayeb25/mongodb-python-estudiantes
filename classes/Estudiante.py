from classes import DbMongo
class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "estudiante"

    def save(self, db):
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)