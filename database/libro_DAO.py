from database.DB_connect import DBConnect
from model.libro_DTO import Libro


"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO


    def read_libro(self):
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is None:
            return None

        query = "SELECT id,titolo,autore,genere,anno_pubblicazione,id_biblioteca FROM libro"
        cursor = cnx.cursor()
        cursor.execute(query)

        result = []
        for row in cursor:
            libro = Libro(*row)
            result.append(libro)

        cursor.close()
        cnx.close()
        return result