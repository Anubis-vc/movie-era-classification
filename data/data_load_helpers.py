import os
import requests
import time
from dotenv import load_dotenv 

SAVE_DIR = "posters"
os.makedirs(SAVE_DIR, exist_ok=True)
load_dotenv()

'''
Queries TMDB API to retrieve movie data by year based on revenue. Retries 5 times
by default and respects 429 status codes for rate limiting

Args:
    - year(int): year for movies
    - page(int): desired page number from data

Return:
    - JSON response from TMDP API (read docs for structure)
'''
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

'''
Takes path to a TMDB movie poster jpg, grabs the mid-sized version (w500) for space, 
creates a filename based on the tmdb id. Saves to data directory and returns filename
if download was successful.

Args:
    - movie_id (string): TMDB movie ID
    - poster_path (string): link to the poster hosted on TMDB
Returns:
    - filename (string): name of downloaded image file
'''
def download_poster(movie_id, poster_path):
    if not poster_path:
        return None
    url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    try:
        img_data = requests.get(url).content
        filename = f"{movie_id}.jpg"
        with open(os.path.join(SAVE_DIR, filename), "wb") as f:
            f.write(img_data)
        return filename
    except Exception as e:
        print(f"Download failed, skipping: {e}")
        return None

'''
Perfroms processing for all the pages for a given year

Args:
    - year (int): release year of movie
Returns:
    - year_metadata (List[Dict]): a list of dictionaries that contains the filename of the downloaded image, 
        the title of the movie, and the year it was released
'''
def process_year(year: int):
    year_metadata = []
    for page in range(1, 4):
        try:
            movies = get_movies_by_year(year, page)
            
            # extract results array from json response
            for movie in movies.get("results", []):
                
                # extract id and poster for each movie for downloading
                id = movie.get('id')
                poster_path = movie.get('poster_path', '')
                filename = download_poster(id, poster_path)
                
                # adding title for fun and for possible debugging
                title = movie.get('title', '')
                
                # if successful download, add metadata as dictionary
                if filename:
                    year_metadata.append({
                        "filename": filename,
                        "title": title,
                        "release_year": year
                    })
        except Exception as e:
            print(f"error at {year}, page {page}, movie{title}")
    return year_metadata