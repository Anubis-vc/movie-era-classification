import os
import requests
from dotenv import load_dotenv 

SAVE_DIR = "posters"
os.makedirs(SAVE_DIR, exist_ok=True)
load_dotenv()

# TODO: RESPECT 429 CODE
def get_movies_by_year(year, page=1):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": os.getenv("TMDB_API_KEY"),
        "sort_by": "revenue.desc",
        "primary_release_year": year,
        "page": page,
    }
    res = requests.get(url, params=params)
    return res.json()

def download_poster(movie_id, poster_path):
    if not poster_path:
        return None
    url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    img_data = requests.get(url).content
    filename = f"{movie_id}.jpg"
    with open(os.path.join(SAVE_DIR, filename), "wb") as f:
        f.write(img_data)
    return filename