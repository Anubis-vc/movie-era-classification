from threaded import run_threaded
from non_threaded import run_non_threaded
import os

non_threaded_time = run_non_threaded()

try:
    folder_path = "folderpath/poster"
    for item in os.listdir(folder_path):
        path = os.path.join(folder_path, item)
        os.remove(path)
    os.remove("folderpath/metadata.csv")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"error: {e}")
    
threaded_time = run_threaded()
percent_decrease = (non_threaded_time - threaded_time) / non_threaded_time * 100

with open("results.txt", "a") as file:
    file.write(f"Non threaded runtime: {non_threaded_time} seconds\n")
    file.write(f"Threaded runtime: {threaded_time} seconds\n")
    file.write(f"Improvement: {percent_decrease}%")
    file.close()