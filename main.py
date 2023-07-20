import datetime
import os

from functions.instagram import client
from functions.joyImageGen import joyceImages
from functions.joyceScraper import goodreadsquotes
from functions.parroty.parroty import Parroty

# server_app = flaskEndpoint.init_flask()
directory = os.getcwd()
# goodreadsquotes.grabber("https://www.goodreads.com/author/quotes/4114218.C_JoyBell_C_")
parroty = Parroty()
parroty.load_model(directory + '/models/joyc7.pt')
res = parroty.generate_text_from_model(' ')
quoteText = '"' + res.strip() + '"'
joyceImages.make_image(f'{quoteText}')

client.make_post('generations/image.jpg', quoteText)

print(f'Posted to Instagram at {datetime.datetime.now()}')
