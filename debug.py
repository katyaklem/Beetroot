import os
import requests
from PIL import Image

URL = 'https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg'


def load_image(url, file_name='example.jpg'):
    image = Image.open(requests.get(url,stream=True).raw)
    image.save(os.path.join(os.getcwd(), file_name))
    image.close()

def print_image_data(file):
    image = Image.open(file)
    print(image.size, image.mode)

def is_square_image(file):
    image = Image.open(file)
    return image.size[0] == image.size[1]
    
def create_thumbnail(file):
    thumbnail_size = (200, 200)
    image = Image.open(file)
    image.thumbnail(thumbnail_size)
    image.save('thumbnail.jpg', 'JPEG')

def is_thumbnail(file):
    thumbnail_size = (200, 133)
    image = Image.open(file)
    print(image.size)
    return image.size[0] == thumbnail_size[0] and image.size[1] == thumbnail_size[1]

def rotate_image(file, degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees)
    rotated.save('rotated.jpg', 'JPEG')

def flip_image(file, direction):
    directions = {'LR': Image.FLIP_LEFT_RIGHT, 'TB':Image.FLIP_TOP_BOTTOM}
    if direction in directions:
        image = Image.open(file)
        out = image.transpose(directions[direction])
        out.save('flipped.jpg', 'JPEG')
    else:
        print('This direction is not correct')

def copy_images_to_dir(dirname):
    for file in os.listdir():
        try:
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.file_name))
        except:
            pass

def create_rectangle_area(file):
    image = Image.open(file)
    image_size = image.size
    crop_size = (200, 133)
    image_crop = image.crop((200, 100, 400, 200))
    print(image_crop.size)
    image_crop.save('crop1.jpg', 'JPEG')

def delete_images():
    for file in os.listdir():
        if file.endswith('.jpg'):
            os.remove(file)

'''
if __name__ == '__main__':
    delete_images()
'''

if __name__ == '__main__':
    print(requests.get(URL).status_code == 200)
    load_image(URL)
    print_image_data('example.jpg')
    print(is_square_image('example.jpg'))
    create_thumbnail('example.jpg')
    print(is_thumbnail('thumbnail.jpg'))
    print(is_thumbnail('example.jpg'))
    rotate_image('example.jpg', 45)
    flip_image('example.jpg', 'RR')
    flip_image('example.jpg', 'LR')
    copy_images_to_dir('images')
    create_rectangle_area('example.jpg')
    print('Done!')
