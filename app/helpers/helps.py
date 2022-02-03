def verify_key(data, keys):
    for key in data.keys():
        if key not in keys:
            return {
                "available_keys": keys,
                "wrong_keys_sended": [key]
            }