import pymongo

from classes import Estudiante, DbMongo

def main():
    db = DbMongo.getDB()
    estudiante = Estudiante("Uayeb 3","Caballero","31487539")
    estudiante.save(db)
    
    
if __name__ == "__main__":
    main()



#collection.insert_one({ "nombre": "Ixchel", "telefono": "eeee" })

#for document in collection.find():
    #print(document)


