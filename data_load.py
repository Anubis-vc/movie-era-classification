import os
import requests
import json
from dotenv import load_dotenv
import tqdm

SAVE_DIR = "posters"
os.makedirs(SAVE_DIR, exist_ok=True)
load_dotenv()

def get_movies_by_year(year, page=1):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": os.getenv("TMDB_API_KEY"),
        "primary_release_year": year,
        "page": page,
    }
    res = requests.get(url, params=params)
    return res.json()

def download_poster(poster_path, movie_id):
    if not poster_path:
        return None
    url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    img_data = requests.get(url).content
    filename = f"{movie_id}.jpg"
    with open(os.path.join(SAVE_DIR, filename), "wb") as f:
        f.write(img_data)
    return filename
    
try:
	movies = get_movies_by_year(2023)
	holdovers = movies['results'][3]
	print(holdovers)
	download_poster(holdovers.get('poster_path'), holdovers.get('id'))
 
except Exception as e:
	print(f"Error: {e}")