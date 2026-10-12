import random
import time
import threading

threads = []
files = ["photo.png", "document.txt", "video.mp4", "archive.zip", "music.mp3"]


def download_file(file_name):
    print(f"Початок завантаження {file_name}...")
    time.sleep(random.randint(1, 3))
    print(f"Завершено: {file_name}")

start = time.perf_counter()

for file in files:
    thread = threading.Thread(target= download_file, args= (files,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Загальний час завантаження: {time.perf_counter() - start}")