from classes import Estudiante, DbMongo, Tipoestudiante
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    ####    Eliminamos toda la base de estudiantes para 
    #       no acumular tanta informacion en 
    ####    cada prueba
    Estudiante.delete_all(db)
    Tipoestudiante.delete_all(db)
    ################################

    Tipoestudiante("Primaria").save(db)
    Tipoestudiante("Secundaria").save(db)
    Tipoestudiante("Superior").save(db)

    #################################

    dictTipos = Tipoestudiante.get_dict(db)

    print(dictTipos)

    Estudiante("Uayeb"
                ,"Caballero"
                ,"31487539"
                , dictTipos["Primaria"]).save(db)
    
    Estudiante("Imix"
                ,"Caballero"
                ,"31487539"
                , dictTipos["Superior"]).save(db)


    Estudiante.print_full_report_long_path(db)
    Estudiante.print_full_report_short_path(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()




