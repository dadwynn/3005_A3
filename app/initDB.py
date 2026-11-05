import os
import sys
from pathlib import Path

import psycopg
from psycopg import sql
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent #app directory
load_dotenv(BASE_DIR.parent / ".env") 

SQL_PATH = BASE_DIR.parent / "sql" / "DDL_DML.sql"


DB_INFO = dict(
    host="localhost",
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

#drops and recreates DB
def recreate_database():
    # DROP/CREATE DATABASE can't run inside a transaction, and u can't drop the db you're connected to, so connect to the default "postgres"
    with psycopg.connect(**DB_INFO, dbname="postgres", autocommit=True) as conn: #database in autocommit mode. Each statement must be its own execute().
        conn.execute("DROP DATABASE IF EXISTS studentDB")
        conn.execute("CREATE DATABASE studentDB")
        print("Recreated database")

def init():
    try:
        #deleting and recreating db
        recreate_database()

        #connect to DB
        DB_NAME = os.getenv("DB_NAME")
        with psycopg.connect(**DB_INFO, dbname=DB_NAME) as conn:
            print(f'Connected to database "{DB_NAME}"')

            script = SQL_PATH.read_text(encoding="utf-8")

            #running the sql script (ddl & dml) as a transaction
            with conn.transaction():
                conn.execute(script)

        print("Database init complete")

    except Exception as err:
        print("Init failed:", err)


