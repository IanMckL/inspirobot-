import os
from instagrapi import Client
from dotenv import dotenv_values, load_dotenv

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

print(username, password)


def make_post(photoPath, text):
    cl = Client()
    try:
        cl.login(f'{username}', f'{password}')
        cl.photo_upload(photoPath, f'{text}')
    except RuntimeError:
        print('Oops,')

