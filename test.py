from rembg import remove
from PIL import Image
inputer = Image.open('me.jpg')	
outputer = remove(inputer)
outputer.save('output_image.jpg')
print('success')
