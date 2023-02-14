import requests
import os
from requests.structures import CaseInsensitiveDict
from app.models.tv_show import TVShow

TMDB_URL = "https://api.themoviedb.org/3/"
token = os.environ.get("TMDB_BEARER_TOKEN")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

def get_TMDB_tv_show(tmdb_id):
    url = f"{TMDB_URL}tv/{tmdb_id}"
    response = requests.get(url,headers=headers)
    print("Getting this response: ")
    print(response.json())

    response.raise_for_status()

    tv_show= TVShow.from_dict(response.json())

    return tv_show

