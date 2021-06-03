import requests
url = r'https://png.pngtree.com/png-clipart/20191129/ourlarge/pngtree-watercolor-flowers-bouquet-with-outlined-glitter-leaves-decoration-png-image_2039586.jpg'

get_image = requests.get(url).content

with open('flr.png', 'wb') as f:
    f.write(get_image)