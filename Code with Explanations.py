import requests

#the link must be ends with .jpg or .jpeg or another image formates
url = r'https://png.pngtree.com/png-clipart/20191129/ourlarge/pngtree-watercolor-flowers-bouquet-with-outlined-glitter-leaves-decoration-png-image_2039586.jpg'

#it will get the bytes of the image
get_image = requests.get(url).content

#it will write the bytes in the specified image and formate
with open('flr.png', 'wb') as f:
    f.write(get_image)
