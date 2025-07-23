#### Modulo para buscar informações do banco de dados

from .data_database import DataGet
import os
import mysql.connector

DB_NAME = "database_detect"
TABLE_NAME_INFO = "info_object"

class InfoData:
    
    def __init__(self):
        self.connection_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv('PASSWORD_DB'),
        database=DB_NAME
        )

        self.create_database_info()
        self.insert_default_objects()

    def create_database_info(self):
        # Creation of the database containing
        # The information about the object to be detected
        connection = self.connection_db

        cursor = connection.cursor()

        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME_INFO} "
            "("
            "id INTEGER NOT NULL AUTO_INCREMENT, "
            "object_detect VARCHAR(100) NOT NULL UNIQUE, "
            "description_object VARCHAR(1000) NOT NULL, "
            "link_object VARCHAR(1000) NOT NULL, "
            "PRIMARY KEY (id)"
            ")"
        )

        cursor.close()

    def insert_into_database(self, object_detect, description_object, link_object):

        conn = self.connection_db
        cursor = conn.cursor()

        sql = f'''
        INSERT INTO {TABLE_NAME_INFO} (object_detect, description_object, link_object) VALUES (%s, %s, %s)
        '''

        cursor.execute(sql,(object_detect, description_object, link_object))
        conn.commit()

        cursor.close()


    def get_info(self):
        
        conn = self.connection_db
        cursor = conn.cursor()

        sql = f'SELECT * FROM {TABLE_NAME_INFO}'
        cursor.execute(sql)
        data_info = cursor.fetchall()

        list_data = []

        for row in data_info:
            _id, object_detect, description_object, link_object = row
            list_data.append(
                [object_detect, description_object, link_object]
            )

        cursor.close()

        return list_data


    def get_detectable_objects(self):
        
        conn = self.connection_db
        cursor = conn.cursor()

        sql = f"SELECT DISTINCT object_detect FROM {TABLE_NAME_INFO}"
        cursor.execute(sql)
        results = cursor.fetchall()

        cursor.close()

        return [row[0] for row in results] or ["pessoa", "telemóvel"]
    

    def insert_default_objects(self):

        conn = self.connection_db
        cursor = conn.cursor()

        # Checks if data already exists
        cursor.execute(f"SELECT object_detect FROM {TABLE_NAME_INFO}")
        existing_objects = [row[0] for row in cursor.fetchall()]

        default_objects = [
            (
                "pessoa", 
                "Uma pessoa qualquer foi detectada.", 
                "https://pt.wikipedia.org/wiki/Pessoa"
            ),
            (
                "telemóvel", 
                "Não sei a marca deste telemóvel.", 
                "https://pt.wikipedia.org/wiki/Telefone_celular"
            )
        ]

        for obj, desc, link in default_objects:
            if obj not in existing_objects:
                cursor.execute(
                    f"""
                    INSERT INTO {TABLE_NAME_INFO} 
                    (object_detect, description_object, link_object) 
                    VALUES (%s, %s, %s)
                    """,
                    (obj, desc, link)
                )

        conn.commit()
        cursor.close()

    def close_connection(self):
        if self.connection_db.is_connected():
            self.connection_db.close()