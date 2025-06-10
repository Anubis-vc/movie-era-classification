from tqdm import tqdm
import datetime
from data_load_helpers import get_movies_by_year, download_poster
# import csv

metadata = []
for year in tqdm(range(1930, datetime.datetime.now().year + 1)):
    for page in range(1, 4):
        try:
            movies = get_movies_by_year(year, page)
            for movie in movies.get("results", []):
                id = movie.get('id')
                poster_path = movie.get('poster_path', '')
                release_date = movie.get('release_date', '')
                download_poster(id, poster_path)
                if id and release_date:
                    metadata.append(
                        {"id": id, "release_year": release_date[:4]})
        except Exception as e:
            print(f"error at {year}, page {page}")