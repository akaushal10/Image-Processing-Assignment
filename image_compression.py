from PIL import Image
img = Image.open(r".\burgur.jpg")
img_name = img.filename[2:]
img.save("Compressed_"+img_name, optimize=True, quality=10)