from flask import jsonify, request
from app.models.anime_model import Anime
from psycopg2.errors import UniqueViolation


keys = ["anime", "released_date", "seasons"]
def save_new_anime():
    data = request.get_json()

    try:
        new_anime = Anime(**data)
        inserted_anime = new_anime.insert_anime()
    except UniqueViolation as err:
        return {"error": "anime is already exists"}
    
    except KeyError as erro:
        for key in data.keys():
            if key != keys:
                return {
                    "available_keys": keys,
                    "wrong_keys_sended": [key]
                }
    
    anime_serialized = Anime.serialize_data(inserted_anime)

    return jsonify(anime_serialized),201

def get_all_animes():
    animes = Anime.get_all()
    animes_serialized = Anime.serialize_data(animes)

    return jsonify({"data": animes_serialized}),200

def get_one_anime(anime_id):
    anime = Anime.get_anime_by_id(anime_id)
    try:
        if anime is None:
            raise
        anime_returned = Anime.serialize_data(anime)
        return jsonify({"data": [anime_returned]})
    except:
        return {"error": "Not Found"}, 404