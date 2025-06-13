# below is only for this folder so we can access data helpers
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/')))

from tqdm import tqdm
import datetime
import time
from data_load_helpers import process_year
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_threaded():
	start_time = time.time()
	metadata = []
	years = range(2022, datetime.datetime.now().year + 1)
	workers = 4

	with ThreadPoolExecutor(max_workers=workers) as executor:
		futures = [executor.submit(process_year, year) for year in years]
		
		for future in tqdm(as_completed(futures), total=len(years)):
			try:
				year_data = future.result()
				metadata.extend(year_data)
			except Exception as e:
				print(f"Some year failed, {e}")

	with open("metadata.csv", "w") as file:
		writer = csv.DictWriter(file, fieldnames=["filename" ,"title", "release_year"])
		writer.writeheader()
		writer.writerows(metadata)
		
	end_time = time.time()

	return end_time - start_time