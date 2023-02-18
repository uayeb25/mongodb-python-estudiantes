from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    #estudiante = Estudiante("Uayeb 3"
    #                        ,"Caballero"
    #                        ,"31487539")
    #estudiante.save(db)

    #estudiante.apellido = "caballero rodriguez"

    #estudiante.update(db)

    #estudiante.delete(db)

    lista_estudiantes = Estudiante.get_list(db)
    lista_estudiantes[0].delete(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()




