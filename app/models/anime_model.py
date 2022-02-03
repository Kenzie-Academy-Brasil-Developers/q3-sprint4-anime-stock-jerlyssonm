from app.models import DataBaseConnect
from psycopg2 import sql


class Anime(DataBaseConnect):    
    base_keys= ["anime", "released_date", "seasons"]
    used_keys= ["id", "anime", "released_date", "seasons"]

    def __init__(self, **kwargs):
        self.anime = kwargs["anime"].title()
        self.released_date = kwargs["released_date"]
        self. seasons = kwargs["seasons"]

    
    def insert_anime(self):
        self.create_table()
        self.get_conn_cur()

        query = """
            INSERT INTO animes(
                anime, released_date, seasons
            )
            VALUES (%s, %s, %s)
            RETURNING *;
        """ 
        query_value = list(self.__dict__.values())

        self.cur.execute(query, query_value)
        inserted_anime = self.cur.fetchone()

        self.commit_and_close()
        return inserted_anime
    
    @classmethod
    def get_all(cls):
        cls.create_table()
        cls.get_conn_cur()

        cls.cur.execute("SELECT * FROM animes")

        all_animes = cls.cur.fetchall()

        cls.commit_and_close()
        return all_animes


    @classmethod
    def get_anime_by_id(cls, anime_id):
        cls.get_conn_cur()

        query = f"""
            SELECT *
            FROM    animes
            WHERE id = {anime_id}
        """
        cls.cur.execute(query)
        anime = cls.cur.fetchone()
        cls.commit_and_close()

        return anime
        

    @classmethod
    def update_anime_info(cls, anime_id, payload):
        cls.get_conn_cur()

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]

        query = sql.SQL(
            """
                UPDATE
                    animes
                SET
                    ({columns}) = ROW({values})
                WHERE
                    id = {id}
                RETURNING *
            """
        ).format(
            id = sql.Literal(anime_id),
            columns = sql.SQL(",").join(columns),
            values = sql.SQL(",").join(values),
        )

        cls.cur.execute(query)
        update_anime = cls.cur.fetchone()
        cls.commit_and_close()

        return update_anime            


    @classmethod
    def delete_anime_by_id(cls, anime_id:int):
        cls.get_conn_cur()

        query = f"""
            DELETE FROM animes
            WHERE id = {anime_id}
            RETURNING *;
        """
        cls.cur.execute(query)
        anime = cls.cur.fetchone()
        cls.commit_and_close()
        return anime


    @staticmethod
    def serialize_data(data, keys= used_keys):
        if type(data) is tuple:
            return dict(zip(keys, data))
        if type(data) is list:
            return [dict(zip(keys, anime)) for anime in data]

