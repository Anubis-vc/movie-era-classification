from tqdm import tqdm
import datetime
import time
from data_load_helpers import *
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

# timing runtime
start_time = time.time()

# metadata to store movie info, years to iterate by year to get even spread, and setting number of threads
metadata = []
years = range(1939, datetime.datetime.now().year + 1)
workers = 20

# use thread manager to control spawn of max_workers number of threads
with ThreadPoolExecutor(max_workers=workers) as executor:
        # submit tasks to thread manager and allow for processing
        futures = [executor.submit(process_year, year) for year in years]
        
        # as tasks complete, collect its metadata result
        # the process_year fxn already downloads the image 
        for future in tqdm(as_completed(futures), total=len(years)):
            try:
                year_data = future.result()
                # add year's metadata to overall metadata
                metadata.extend(year_data)
            except Exception as e:
                print(f"Year failed, {e}")
            

# convert metadata to csv for later processing
with open("metadata.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["filename" ,"title", "release_year", "genres"])
    writer.writeheader()
    writer.writerows(metadata)

# print total runtime
end_time = time.time()
print(f"{end_time - start_time} s")