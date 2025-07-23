## Criação da tabela "object_detect" na base de dados database_detect ## 

import os
from pathlib import Path
import dotenv
import mysql.connector
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
DOTENV_PATH = BASE_DIR / 'dotenv_files/.env'

DB_NAME = 'database_detect'
TABLE_NAME = 'object_detect'

dotenv.load_dotenv(DOTENV_PATH)

class DataGet:

    def __init__(self):
        
        self._create_database()

        # Establish database connection on initialization
        self.connection_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv('PASSWORD_DB'),
        database=DB_NAME
        )

        self._create_table_get()

    def _create_database(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=os.getenv("PASSWORD_DB"),
        )

        cursor = conn.cursor()
        cursor.execute(
            f'CREATE DATABASE IF NOT EXISTS {DB_NAME} '
            )

        conn.commit()
        cursor.close()

    def _create_table_get(self):
        connection = self.connection_db
        cursor = connection.cursor()

        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            object_detect VARCHAR(100) NOT NULL, 
            date_detect VARCHAR(100) NOT NULL 
            )
            """
        )

        cursor.close()

    def save_in_database(self, object_detect):

        # Public method to save a detected object with the current date
        date_detect = str(datetime.now())[:16]
        entry = [object_detect, date_detect]
        
        if not self._entry_exists(entry):
            self._insert_entry(entry)


    def _entry_exists(self, entry):
        # Check if an object-detection entry already exists in the database
        all_data = self.get_data()
        return entry in all_data


    def _insert_entry(self, entry):
        # Insert a new detection entry into the database.
        object_detect, date_detect = entry

        conn = self.connection_db
        cursor = conn.cursor()

        try:

            
            sql = f"""
            INSERT INTO {TABLE_NAME} (object_detect, date_detect) 
            VALUES (%s, %s)
            """
        
            cursor.execute(sql, (object_detect, date_detect))
            conn.commit()

        except mysql.connector.errors.IntegrityError:
            # Ignore duplicate or constraint violations
            pass

        finally:
            cursor.close()


    def get_data(self):
        # Fetch all detection records from the database

        conn = self.connection_db
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        results = cursor.fetchall()

        data = [[obj, date] for obj, date in results]

        cursor.close()

        return data

    def close_connection(self):
        if self.connection_db.is_connected():
            self.connection_db.close()
