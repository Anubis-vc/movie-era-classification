import os
import requests
import time
from dotenv import load_dotenv 

SAVE_DIR = "posters"
os.makedirs(SAVE_DIR, exist_ok=True)
load_dotenv()

def get_movies_by_year(year, page=1, max_attempts=5):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": os.getenv("TMDB_API_KEY"),
        "sort_by": "revenue.desc",
        "primary_release_year": year,
        "page": page,
    }
    
    for _ in range(max_attempts):
        res = requests.get(url, params=params)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 429:
            retry_after = int(res.headers.get("Retry-After", 5))
            print(f"Returned 429, retrying after {retry_after} seconds")
            time.sleep(retry_after)
        else:
            print(f"Request failed: {res.status_code}: {res.text}")
    return {}

def download_poster(movie_id, poster_path):
    if not poster_path:
        return None
    url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    img_data = requests.get(url).content
    filename = f"{movie_id}.jpg"
    with open(os.path.join(SAVE_DIR, filename), "wb") as f:
        f.write(img_data)
    return filename