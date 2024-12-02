#pip install pillow
from PIL import Image, ImageDraw
import io
import random

def generate_image(size_b, ext='png'):
  # Calculate number of pixels to achieve the required size
  height = 1
  if ext == 'png':
    size = size_b // 4
    if size == 0:
      size = 1
  elif ext == 'jpeg':
    height = 480
    size = size_b
    if size == 0:
      size = 1        

  image = Image.new('RGB', (height, size), color='blue')

  if ext == 'jpeg':
    draw_image = ImageDraw.Draw(image)
    for i in range(height):
      for j in range(size):
        draw_image.point((i, j), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))              )

  # Save the image
  with io.BytesIO() as output:
    image.save(output, format=ext, compress_level=0, quality=100)

    with open(str(size_b) + '.' + ext, 'wb') as f:
      f.write(output.getvalue())

# not exact size
# generate_image(100, 'png')
# generate_image(10000, 'png')
# generate_image(2097152 - 772 + 16, 'png') #2096396, actual 2097151
# generate_image(2097152 - 772 + 20, 'png') #2096400, actual 2097155
generate_image(5000000, 'png')

# generate_image(100, 'jpeg')
# generate_image(1000, 'jpeg')
# generate_image(2000, 'jpeg')
# generate_image(2210, 'jpeg')
# generate_image(2209, 'jpeg')
# generate_image(2208, 'jpeg')
generate_image(5000, 'jpeg')