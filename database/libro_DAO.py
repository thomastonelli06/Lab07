from database.DB_connect import DBConnect
from model.libro_DTO import Libro


"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass


    def read_libro(self, id_bibl , genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        query = ("SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca "
                 "FROM libro "
                 "WHERE genere = COALESCE(%s, genere) "
                 "AND id_biblioteca = COALESCE(%s, id_biblioteca)")
        cursor = cnx.cursor()
        cursor.execute(query, (genere, id_bibl))


        result = []
        for row in cursor:
            libro = Libro(*row)
            result.append(libro)

        cursor.close()
        cnx.close()
        return result

    def read_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        query = ("SELECT DISTINCT genere"
                 "FROM libro "
                 )
        cursor = cnx.cursor()
        cursor.execute(query)

        generi = []
        for row in cursor:

            generi.append(row)

        cursor.close()
        cnx.close()
        return generi