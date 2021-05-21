from PIL import Image
from PIL import ImageFilter

img1=Image.open("License plate.jpg")

img2=img1.filter(ImageFilter.EDGE_ENHANCE)
img2.save("out11.jpg")
img3=img2.filter(ImageFilter.EMBOSS)
img3.save("out12.jpg")
img5=img3.filter(ImageFilter.SMOOTH)
img5.save("out14.jpg")
img6=img5.filter(ImageFilter.SMOOTH_MORE)
img6.save("out15.jpg")