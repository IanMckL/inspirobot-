import os
from threading import Thread
from blather import Blather
from functions.joyImageGen import joyceImages
from functions.joyceScraper import goodreadsquotes
from functions.instagram import client
from functions.flask import flaskEndpoint


server_app = flaskEndpoint.init_flask()
directory = os.getcwd()
# goodreadsquotes.grabber("https://www.goodreads.com/author/quotes/4114218.C_JoyBell_C_")
blather = Blather()
# blather.read('joyce.txt')
# blather.save('joyc7.pt')
blather.load(directory + '/models/joyc7.pt')

res = ""
while len(res) < 45 or len(res) > 250:
    res = blather.write(' ')
quoteText = '"' + res.strip() + '"'
joyceImages.make_image(f'{quoteText}')

client.make_post('generations/image.jpg', quoteText)
# if using ngrok in a virtual environment, use os.chmod(executable, 755) on line 29 of flask_ngrok.py
