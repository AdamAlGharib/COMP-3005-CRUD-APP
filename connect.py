import psycopg2

def get_conn():

    try:
        return psycopg2.connect(
            host="localhost",
            database="assignment2",
            user="postgres",
            port="5432"
        )

    except:
        print("Connection to Postgres has failed")