from http import HTTPStatus
from flask import jsonify, request
from app.helpers.helps import verify_key
from app.models.anime_model import Anime
from psycopg2.errors import UniqueViolation, UndefinedColumn


keys = Anime.base_keys
def save_new_anime():
    data = request.get_json()
    try:
        new_anime = Anime(**data)
        inserted_anime = new_anime.insert_anime()
    except UniqueViolation:
        return {"error": "anime is already exists"}, HTTPStatus.UNPROCESSABLE_ENTITY
    except KeyError:
        return verify_key(data, keys),HTTPStatus.UNPROCESSABLE_ENTITY

    anime_serialized = Anime.serialize_data(inserted_anime)
    return jsonify(anime_serialized), HTTPStatus.CREATED


def get_all_animes():
    animes = Anime.get_all()
    try:
        if animes is None:
            raise        
        animes_serialized = Anime.serialize_data(animes)
        return jsonify({"data": animes_serialized}),HTTPStatus.OK
    except:
        return {"data": []}, HTTPStatus.OK


def get_one_anime(anime_id):
    anime = Anime.get_anime_by_id(anime_id)
    try:
        if anime is None:
            raise
        anime_returned = Anime.serialize_data(anime)
        return jsonify({"data": [anime_returned]}), HTTPStatus.OK
    except:
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND


def update_info_anime(anime_id):
    payload = request.get_json()

    try:
        updated_anime = Anime.update_anime_info(anime_id, payload)
        if not updated_anime:
            return {"error": "Not Found"}, HTTPStatus.NOT_FOUND
        serialized_anime = Anime.serialize_data(updated_anime)
        return jsonify(serialized_anime), HTTPStatus.OK
    
    except UndefinedColumn:
        return verify_key(payload, keys),HTTPStatus.UNPROCESSABLE_ENTITY


def delete_anime(anime_id: int):
    try:
        anime = Anime.delete_anime_by_id(anime_id)
        if anime is None:
            raise
        return '', HTTPStatus.NO_CONTENT
    except:
        return {"error": "Not Found"},HTTPStatus.NOT_FOUND