from tqdm import tqdm
import datetime
import time
from data.data_load_helpers import process_year
import csv

start_time = time.time()
metadata = []

# testing on limited dataset
for year in tqdm(range(2020, datetime.datetime.now().year + 1)):
    process_year(year)

# convert metadata to csv for later processing
with open("metadata.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["filename" ,"title", "release_year"])
    writer.writeheader()
    writer.writerows(metadata)
    
end_time = time.time()

with open("times.txt", "a") as file:
    file.write(f"non-threaded took f{end_time - start_time} seconds to complete")