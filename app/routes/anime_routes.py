from flask import Blueprint

from app.controllers.anime_controller import get_all_animes, get_one_anime, save_new_anime


bp_anime = Blueprint("animes", __name__, url_prefix="/animes")

bp_anime.post("")(save_new_anime)
bp_anime.get("")(get_all_animes)
bp_anime.get("/<anime_id>")(get_one_anime)
bp_anime.patch("/<anime_id>")(save_new_anime)
bp_anime.delete("/<int:anime_id>")(save_new_anime)
