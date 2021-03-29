#!/usr/bin/env python3

import os
from PIL import Image

if os.path.isfile("sw.png"):
    with Image.open('sw.png') as img:
        img.show()

else:
    import requests
    file_url = "https://raw.githubusercontent.com/NickTheDick69/sw/main/sw.png"
    r = requests.get(file_url)
    with open("sw.png", "wb") as f:
        f.write(r.content)
    with Image.open('sw.png') as img:
        img.show()
