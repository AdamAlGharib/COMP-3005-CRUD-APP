import psycopg2
import os

def get_conn():

    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "assignment2"),
            user=os.getenv("DB_USER", "postgres"),
            port=os.getenv("DB_PORT", "5432")
        )

    except:
        print("Connection to Postgres has failed")