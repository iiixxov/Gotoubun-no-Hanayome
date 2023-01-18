import glob
from PIL import Image


img_names = glob.glob("C:\\renpy\\Gotoubun no Hanayome\\game\\images\\backgrounds\\*.png")

for i, img_name in enumerate(img_names):
    image = Image.open(img_name)
    if image.size != (1920, 1080):
        short_name = img_name[img_name.rfind('\\') + 1:]
        print(f'"{short_name}" processing')
        image = image.resize((1920, 1080))
        image.save(img_name)
        