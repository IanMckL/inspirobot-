import os
from instagrapi import Client
from dotenv import dotenv_values, load_dotenv

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
cl = Client()


def make_post(photo_path, text):
    try:
        cl.login(f'{username}', f'{password}')
        cl.photo_upload(photo_path, f'{text}')
    except(RuntimeError, Exception):
        print('Instagram login error')
        pass


def make_message(userid="", message="wuwu", name=""):
    user = cl.user_info_by_username('zer0_117')
    cl.direct_send(f'{message}', [user.pk])
