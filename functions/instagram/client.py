import os
import time
import uuid

from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
client_session_id = str(uuid.uuid4())


settings = {'uuids': {'phone_id': '2ce164f3-cbb2-4186-8f76-baea0e5eb440', 'uuid': 'fd35b4e9-409c-472d-b0cc-9079f6a536b2', 'client_session_id': '82b22c01-b1de-40d5-bfdc-c8b2f98cfad8', 'advertising_id': 'b23f6498-ac04-4f1d-b7e6-704d9474d2f8', 'android_device_id': 'android-720eeb7e28234ffb', 'request_id': '7bfe6be6-0563-4bc6-a023-fcc09686755d', 'tray_session_id': 'f216c939-fa82-4c40-8ad2-1bab0344ebb6'}, 'mid': 'ZLiNiQABAAFsgzCDtbkhVTxNsorE', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '60805134309', 'sessionid': '60805134309%3Ax9AAE9NTUTgM65%3A13%3AAYdv3uZ5n4YjSQgtL5zNZTkzOIQ0I6lEz0IpJawV0w'}, 'cookies': {}, 'last_login': 1689816466.0005498, 'device_settings': {'app_version': '269.0.0.18.75', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'OnePlus', 'device': 'devitron', 'model': '6T Dev', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 269.0.0.18.75 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; 6T Dev; devitron; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400}


cl = Client()
cl.delay_range = [2, 3]

def make_post(photo_path, text):
    try:
        print(f'{username}')
        cl.login(f'{username}', f'{password}')
        print(cl.get_settings())
        cl.photo_upload(photo_path, f'{text}')
    except(RuntimeError, Exception):
        print('Instagram login error')
        pass


def make_message(userid="", message="wuwu", name=""):
    user = cl.user_info_by_username('zer0_117')
    cl.direct_send(f'{message}', [user.pk])


# WARNING: Instagram is very cautious and will flag accounts they suspect
# are scraping user data. Which we technically /are/ doing. Use sparingly.
def get_all_followers_array():
    my_id = cl.user_id
    followers = cl.user_followers(str(my_id))
    follower_array =[]
    for follower in followers:
        follower_array.append(follower)
    return follower_array


def new_followers_check():
    current_followers_list = get_all_followers_array()
    old_followers_list = get_followers_txt_array()

    for follower in current_followers_list:
         if follower in old_followers_list:
             continue
         else:
            print("initiate welcome sequence for ", follower)


def joy_routine():
    # Check if there are new followers. If there are, send them a new message
    new_followers_check()
    # Erase the old followers list and update it with all new users
    update_follower_list()


def get_followers_txt_array():
    user_array = []
    with open(os.getcwd()+'/followers.txt', 'r') as file:
        content = file.read().split('\n')
        for line in content:
            user_array.append(line)
    return user_array



def erase_follower_list():
    print(os.getcwd())
    with open(os.getcwd() + '/followers.txt','w+') as file:
        file.truncate(0)


def update_follower_list():
    erase_follower_list()
    followers = get_all_followers_array()
    for follower in followers:
        print("follower: ", follower)
        with open(os.getcwd() + '/followers.txt', 'a') as file:
            file.writelines(follower + "\n")



