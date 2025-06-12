from tqdm import tqdm
import datetime
from data_load_helpers import get_movies_by_year, download_poster
import csv

metadata = []

# grab the 60 top grossing movies from each year to add to dataset
for year in tqdm(range(1939, datetime.datetime.now().year + 1)):
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
                    metadata.append({
                        "filename": filename,
                        "title": title,
                        "release_year": year
                    })
        except Exception as e:
            print(f"error at {year}, page {page}, movie{title}")

# convert metadata to csv for later processing
with open("metadata.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["filename" ,"title", "release_year"])
    writer.writeheader()
    writer.writerows(metadata)