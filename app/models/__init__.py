import psycopg2
from os import getenv


configs = {
    "host": getenv("DB_HOST"),
    "database": getenv("DB_NAME"),
    "user": getenv("DB_USER"),
    "password": getenv("DB_PASSWORD")
}

class DataBaseConnect:

    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()

    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def create_table(cls):
        cls.get_conn_cur()

        cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS animes(
                id          BIGSERIAL   PRIMARY KEY,
                anime       VARCHAR(100)    NOT NULL    UNIQUE,
                released_date   DATE    NOT NULL,
                seasons         INTEGER NOT NULL
            )
        """)

        cls.commit_and_close()
        return {"date": []}