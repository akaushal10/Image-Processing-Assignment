from PIL import Image
import matplotlib.pyplot as plt
ImageAddress = 'burgur.jpg'
imageFile = Image.open(ImageAddress)
print(ImageAddress," is opening")
print("After 5 seconds it will be closed")
plt.imshow(imageFile)
plt.draw()
plt.pause(5)
plt.close()
print(ImageAddress," has been closed")