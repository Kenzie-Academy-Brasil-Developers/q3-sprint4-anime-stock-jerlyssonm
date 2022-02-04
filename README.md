# API for delivery 13 - Anime_Stock

**1** : to get started install requirements.txt, within your virtual environment "pip3 install -r requirements.txt"

## since it is a simple API, let's get down to business

*List of EndPoints*

- GET /animes
- GET /animes/id
- POST /animes
- PATCH /animes/id
- DELETE /animes/id

**Usage examples with some necessary data**

# GET /animes with data
![with data](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/get/get.png)

# GET /animes no data
![no data](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/get/get_sem_tabela.png)

# GET /animes/id with id Exist
![get](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/get/get_by_id.png)

# GET /animes/id with id non-Existent
![get](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/get/get_by_id_sem_tabela.png)


# POST /animes with correct data
![post](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/post/post.png)

# POST /animes incorrect date
![post](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/post/post_invalid_keys.png)

# POST /animes with existing data
![post](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/post/post_already_exists.png)

# PATCH /animes/id with correct keys
![patch](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/patch/patch.png) 

# PATCH /animes/id with incorrect keys
![patch](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/patch/patch_chaves_invalidas.png)

# PATCH /animes/id with non-existent id
![patch](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/patch/patch_sem_tabela.png)

# DELETE /animes/id with id exist
![delete](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/delete/delete.png)

# DELETE /animes/id with non-existent id
![delete](https://gitlab.com/chrystian14/anime-stock-returns/-/raw/main/imgs/delete/delete_sem_tabela.png)