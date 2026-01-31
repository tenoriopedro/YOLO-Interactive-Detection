import os
from datetime import datetime
from pathlib import Path

import dotenv
import mysql.connector

from yolo_detector.config import DB_HOST, DB_USER, DB_PASSWORD


DB_NAME = "database_detect"
TABLE_NAME = "object_detect"


class DetectionStorage:

    def __init__(self) -> None:
        self._create_database()

        # Establish database connection on initialization
        self.connection_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("PASSWORD_DB"),
            database=DB_NAME
        )

        self._create_table_get()

    def _create_database(self) -> None:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("PASSWORD_DB"),
        )

        cursor = conn.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {DB_NAME} "
        )

        conn.commit()
        cursor.close()

    def _create_table_get(self) -> None:
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

        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        results = cursor.fetchall()

        data = [[obj, date] for obj, date in results]

        cursor.close()

        return data

    def show_data_today(self) -> None:
        # Shows the data that was captured that day

        conn = self.connection_db
        cursor = conn.cursor()

        today_str = datetime.now().strftime("%Y-%m-%d")

        query = f"""
        SELECT * FROM {TABLE_NAME}
        WHERE date_detect LIKE %s
        """

        like_pattern = f"{today_str}%"

        cursor.execute(query, (like_pattern,))
        results = cursor.fetchall()

        data = [[obj, date] for obj, date in results]

        cursor.close()

        return data

    def close_connection(self) -> None:
        if self.connection_db.is_connected():
            self.connection_db.close()
