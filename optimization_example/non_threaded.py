# below is only for this folder so we can access data helpers
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/')))

from tqdm import tqdm
import datetime
import time
from data_load_helpers import process_year
import csv

def run_non_threaded():
    start_time = time.time()
    metadata = []

    # testing on limited dataset
    for year in tqdm(range(2022, datetime.datetime.now().year + 1)):
        year_data = process_year(year)
        metadata.extend(year_data)

    # convert metadata to csv for later processing
    with open("metadata.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["filename" ,"title", "release_year"])
        writer.writeheader()
        writer.writerows(metadata)
        
    end_time = time.time()

    return end_time - start_time