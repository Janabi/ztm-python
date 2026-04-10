from PIL import Image, ImageFilter

img = Image.open('./scripting/image-playground/astro.jpg')
img.thumbnail((400, 400))
img.save('./scripting/image-playground/astro-thumbnail.jpg')
print(img.size)