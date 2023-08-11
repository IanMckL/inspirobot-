import os
import threading
import time
import uuid
import random

from dotenv import load_dotenv
from instagrapi import Client
from functions.parroty.parroty import Parroty


load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
client_session_id = str(uuid.uuid4())
parroty = Parroty()


cl = Client()
cl.delay_range = [6, 8]


def login():
    if os.path.isfile(os.getcwd() + '/functions/instagram/session.json'):
        print('session file exists')
        cl.load_settings(os.getcwd() + '/functions/instagram/session.json')
        cl.login(f'{username}', f'{password}')
    else:
        cl.login(f'{username}', f'{password}')
        cl.dump_settings(os.getcwd() + '/functions/instagram/session.json')


def make_post(photo_path, text):
    try:
        cl.photo_upload(photo_path, f'{text}')
    except(RuntimeError, Exception):
        print('Instagram error')
        pass


def make_message(userid="", message="wuwu", name=""):
    user = cl.user_info_by_username('zer0_117')
    cl.direct_send(f'{message}', [user.pk])


# WARNING: Instagram is very cautious and will flag accounts they suspect
# are scraping user data. Which we technically /are/ doing. Use sparingly.
def get_all_followers_array():
    my_id = cl.user_id
    followers = cl.user_followers(str(my_id))
    follower_array = []
    for follower in followers:
        follower_array.append(follower)
    return follower_array


def new_user_onboarding(user_id):
    try:
        user = cl.user_info(user_id)
        cl.direct_send("Hey, are you my new friend?", [user.pk])
    except(RuntimeError, Exception):
        print("Instagram error")
        pass


def new_followers_check():
    current_followers_list = get_all_followers_array()
    old_followers_list = get_followers_txt_array()

    for follower in current_followers_list:
        if follower in old_followers_list:
            continue
        else:
            print("initiate welcome sequence for ", follower)
            new_user_onboarding(follower)


def joy_routine():
    # Check if there are new followers. If there are, send them a new message
    new_followers_check()
    # Erase the old followers list and update it with all new users
    update_follower_list()

def create_random_comment():
    # Find a random post from a random user
    followers = get_all_followers_array()
    # Get a random follower
    random_follower = random.choice(followers)
    # Get one of their posts
    posts = cl.user_medias(random_follower, 100)
    # Get a random post
    random_post = random.choice(posts)
    # Generate a comment from the comment model
    parroty.load_model(os.getcwd() + '/models/joybell_comments.pt')
    comment = parroty.generate_text_from_model(' ')
    # Post comment on random post
    cl.media_comment(random_post.pk, comment)


def get_followers_txt_array():
    user_array = []
    with open(os.getcwd() + '/functions/instagram/followers.txt', 'r') as file:
        content = file.read().split('\n')
        for line in content:
            user_array.append(line)
    return user_array


def delete_follower_list():
    print(os.getcwd())
    with open(os.getcwd() + '/followers.txt', 'w+') as file:
        file.truncate(0)


def update_follower_list():
    delete_follower_list()
    followers = get_all_followers_array()
    for follower in followers:
        print("follower: ", follower)
        with open(os.getcwd() + '/followers.txt', 'a') as file:
            file.writelines(follower + "\n")


def create_story():
    cl.photo_upload_to_story(os.getcwd() + '/generations/image.jpg', 'test')


def scrape_joybell_posts_text():
    joybell = cl.user_info_by_username("cjoybellc")
    posts = cl.user_medias(joybell.pk, 100)
    extracted_post_text = []
    for post in posts:
        extracted_post_text.append(post.caption_text)
    print(extracted_post_text)


def scrape_joybell_comments_text():
    joybell = cl.user_info_by_username("cjoybellc")
    posts = cl.user_medias(joybell, 100)

    extracted_media_ids = []
    extracted_reply_text = []

    for media in extracted_media_ids:
        print("loading media:", media)
        replies = cl.media_comments(media)
        for reply in replies:
            if reply.user.pk == joybell.pk:
                print(reply.text)
                extracted_reply_text.append(reply.text)

    print(extracted_reply_text)
    for reply in extracted_reply_text:
        # remove every word that starts with @
        reply = ' '.join([word for word in reply.split() if not word.startswith('@')])
        print(reply)
        with open(os.getcwd() + '/joybell_comments.txt', 'a') as file:
            file.writelines(reply + "\n")


#   return a true or false value based on change in percentage
def random_chance(percent):
    return random.randrange(100) < percent

def scrape_joybell_followers():
    joybell = cl.user_info_by_username("cjoybellc")
    print(joybell)
    followers = cl.user_followers(joybell.pk, True, 500)
    parroty.load_model(os.getcwd() + '/models/joybell_comments.pt')
    for follower in followers:
        # Get one of their posts
        posts = cl.user_medias(follower, 10)
        # If there are posts
        if posts:
            # Get a random post
            random_post = random.choice(posts)
            # 30 percent chance of liking the post
            if random_chance(30):
                try:
                    cl.media_like(random_post.pk)
                except(RuntimeError, Exception):
                    pass
            # 30 percent chance of following user
            if random_chance(10):
                try:
                    cl.user_follow(follower)
                except(RuntimeError, Exception):
                    pass

            #40 percent chance of commenting on post
            if random_chance(40):
                # Generate a comment from the comment model
                comment = parroty.generate_text_from_model(' ')
                print(comment, follower)
                # Post comment on random post
                try:
                    cl.media_comment(random_post.pk, comment)
                except(RuntimeError, Exception):
                    pass

def trigger_function_on_interval_minutes(minutes, function):
      seconds = minutes * 60
      def execute():
        while True:
            function()
            time.sleep(seconds)

      thread = threading.Thread(target=execute)
      thread.daemon = True
      thread.start()



login()
scrape_joybell_followers()