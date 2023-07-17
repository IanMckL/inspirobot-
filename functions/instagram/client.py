import os
import uuid

from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
client_session_id = str(uuid.uuid4())
cl = Client()
settings = {
    "uuids": {
        "phone_id": "be60e0a9-7201-5492-da04-4f2b85b3b592",
        "uuid": "be60e0a9-7201-5492-da04-4f2b85b3b592",
        "client_session_id": client_session_id,
        "advertising_id": "1c413050-795d-f321-eeb4-4962ca0a731c",
        "device_id": "android-f4f80570fe070b5f"
    },
    "cookies": {},
    "last_login": 1674240519.7862692,
    "device_settings": {
        "cpu": "h1",
        "dpi": "640dpi",
        "model": "C6503",
        "device": "C6503",
        "resolution": "1794x1080",
        "app_version": "117.0.0.28.123",
        "manufacturer": "Sony",
        "version_code": "164321834",
        "android_release": "4.2.2",
        "android_version": 23
    },
    "user_agent": "Opera/9.80 (Android 4.2.2; Linux; Opera Mobi/ADR-1210241554; U; en-us) Presto/2.11.355 Version/12.10"
}


def make_post(photo_path, text):
    try:
        print(f'{username}')
        cl.login(f'{username}', f'{password}')
        cl.photo_upload(photo_path, f'{text}')
    except(RuntimeError, Exception):
        print('Instagram login error')
        pass


def make_message(userid="", message="wuwu", name=""):
    user = cl.user_info_by_username('zer0_117')
    cl.direct_send(f'{message}', [user.pk])
