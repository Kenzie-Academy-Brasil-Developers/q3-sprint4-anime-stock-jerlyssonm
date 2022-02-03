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
        return {"error": "anime is already exists"},422
    
    except KeyError as erro:
        for key in data.keys():
            if key not in keys:
                return {
                    "available_keys": keys,
                    "wrong_keys_sended": [key]
                },422
    
    anime_serialized = Anime.serialize_data(inserted_anime)
    return jsonify(anime_serialized),201

def get_all_animes():
    animes = Anime.get_all()
    if animes is None:
        return {"data": []},200
    
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

def update_info_anime(anime_id):
    payload = request.get_json()
    try:
        updated_anime = Anime.update_anime_info(anime_id, payload)

        if not updated_anime:
            return {"error": "Not Found"},404
        serialized_anime = Anime.serialize_data(updated_anime)
        return jsonify(serialized_anime), 200
    
    except:
        for key in payload.keys():
            if key not in keys:
                return {
                    "available_keys": keys,
                    "wrong_keys_sended": [key]
                },422

def delete_anime(anime_id: int):
    try:
        anime = Anime.delete_anime_by_id(anime_id)
        if anime is None:
            raise
        return '', 204
    except:
        return {"error": "Not Found"},404