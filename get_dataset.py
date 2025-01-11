from pathlib import Path
import shutil
import os
from tqdm import tqdm
import requests
from PIL import Image  # Import thư viện Pillow

ANNOTATION_FOLDER = Path('annotations')
DATA_FOLDER = Path('data')  # Will be created to store images


def check_or_create_folder(folder):
    if os.path.exists(folder):
        print(f"Directory {folder} already exists!")
        if len([f for f in os.listdir(folder) if os.path.isfile(folder / f)]) > 0:
            print("Folder to download images to already exists and is not empty! Not downloading.")
            return False
        return True
    else:
        os.makedirs(folder, exist_ok=True)
        return True


def get_images(train_or_val):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    training_img_links = open(ANNOTATION_FOLDER / (train_or_val + '.txt')).read().splitlines()
    for img_link in tqdm(training_img_links):
        try:
            response = requests.get(img_link, headers=headers, timeout=10)
            response.raise_for_status()  # Gây lỗi nếu không phải HTTP 200
            file_path = DATA_FOLDER / train_or_val / os.path.basename(img_link)
            with open(file_path, 'wb') as handler:
                handler.write(response.content)

            # Kiểm tra ảnh hợp lệ
            with Image.open(file_path) as img:
                img.verify()
        except Exception as e:
            print(f"Failed to download {img_link}: {e}")


if __name__ == '__main__':
    if check_or_create_folder(DATA_FOLDER):
        if check_or_create_folder(DATA_FOLDER / 'train'):
            get_images('train')
        if check_or_create_folder(DATA_FOLDER / 'val'):
            get_images('val')
        shutil.copytree(ANNOTATION_FOLDER, DATA_FOLDER / 'annotations')
