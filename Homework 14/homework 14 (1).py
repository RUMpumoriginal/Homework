import random
import time


files = ["photo.png", "document.txt", "video.mp4", "archive.zip", "music.mp3"]


def download_file(file_name):
    print(f"Початок завантаження {file_name}...")
    time.sleep(random.randint(1, 3))
    return print(f"Завершено: {file_name}")

start = time.perf_counter()

for file in files:
    download_file(file)


print(f"Загальний час завантаження: {time.perf_counter() - start}")