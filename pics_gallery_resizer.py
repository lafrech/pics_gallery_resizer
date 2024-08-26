from pathlib import Path
import argparse
import math

from PIL import Image, ImageOps, UnidentifiedImageError


MAX_WIDTH = math.inf
MAX_HEIGHT = 960

parser = argparse.ArgumentParser()
parser.add_argument('source_dir')
parser.add_argument('destination_dir')
args = parser.parse_args()

SRC_DIR = Path(args.source_dir)
DST_DIR = Path(args.destination_dir)

DST_DIR.mkdir(exist_ok=True)


for pic_f_path in SRC_DIR.iterdir():
    if not pic_f_path.is_file():
        continue

    print(pic_f_path)
    try:
        pic = Image.open(pic_f_path)
    except UnidentifiedImageError:
        continue

    pic = ImageOps.exif_transpose(pic)
    pic = ImageOps.contain(pic, (MAX_WIDTH, MAX_HEIGHT))
    pic.save(DST_DIR / pic_f_path.name)
