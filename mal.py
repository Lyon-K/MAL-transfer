import re
import requests

csrf_token = ""


def mal_add_to_list(
    create_tab,
    anime_id: int,
    status: str = "watching",
    num_watched_episodes: int = 0,
    score: int = 0,
):
    payload = {
        "anime_id": anime_id,
        "status": mal_status_to_int(status),
        "score": num_watched_episodes,
        "num_watched_episodes": score,
        "csrf_token": csrf_token,
    }
    request_url = "https://myanimelist.net/ownlist/anime/edit.json"
    if requests.post(request_url, payload):
        return True
    return False


def mal_status_to_int(status: str):
    # remove all non alphanumeric chars
    status = re.sub("[\W_]+", "", status.lower())
    if status == "watching":
        return 1
    elif status == "completed":
        return 2
    elif status == "onhold":
        return 3
    elif status == "dropped":
        return 4
    elif status == "plantowatch":
        return 6
