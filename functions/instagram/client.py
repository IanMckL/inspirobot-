import os

from blather import Blather
from instagrapi import Client
from dotenv import dotenv_values, load_dotenv
from functions.joyImageGen import joyceImages
from profanityfilter import ProfanityFilter

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
cl = Client()
pf = ProfanityFilter()
directory = os.getcwd()
print(directory)


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


def respond_to_comment(media_id, comment_id, instagram_username="zer0_117", comment=""):
    blather = Blather()
    try:
        user = cl.user_info_by_username(f'{instagram_username}')
    except(RuntimeError, Exception):
        print('Instagram login error')
        pass

    if "write me a poem about " in str(comment).lower():
        subject = comment.lower().split("write me a poem about ")[1].split(' ')[0].capitalize()
        if pf.is_profane(subject):
            return None

        blather.load(directory + '/models/joyc7.pt')
        poem = ""
        while len(poem) < 45 or len(poem) > 250 or pf.is_profane(poem):
            poem = blather.write(f'{subject} ')
        print(poem)
        img = joyceImages.make_image(poem)
        make_comment(media_id, comment_id,instagram_username, poem)


def make_comment(media_id, comment_id, insta_username, text):
    try:
        cl.login(f'{username}', f'{password}')
        cl.media_comment(media_id, text, comment_id)
    except(RuntimeError, Exception):
        print('Instagram login error')
        pass
