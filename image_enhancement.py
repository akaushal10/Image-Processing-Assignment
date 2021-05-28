from PIL import Image, ImageEnhance
im = Image.open(r".\burgur.jpg")

im3 = ImageEnhance.Brightness(im)
imageWithBrighness = im3.enhance(2.0)

im3 = ImageEnhance.Sharpness(imageWithBrighness)
imageWithSharpness = im3.enhance(2.0)

imageWithSharpness.show()
