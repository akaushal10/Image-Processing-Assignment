from PIL import Image, ImageFilter
image = Image.open(r"./burgur.jpg")

image = image.convert("L")

image = image.filter(ImageFilter.FIND_EDGES)
image.show()
# image.save(r"Edge_burgur.jpg")
