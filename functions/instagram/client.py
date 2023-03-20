import os
from random import random
from zalgo_text import zalgo
from instagrapi import Client
from dotenv import dotenv_values, load_dotenv

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
cl = Client()
cl.login(f'{username}', f'{password}')


def make_post(photoPath, text):
    cl.photo_upload(photoPath, f'{text}')


def make_message(userid="", message="wuwu", name=""):
    user = cl.user_info_by_username('zer0_117')
    cl.direct_send(f'{message}', [user.pk])
