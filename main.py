import os
from blather import Blather
from functions.joyImageGen import joyceImages
from functions.joyceScraper import goodreadsquotes
from functions.instagram import client
dir = os.getcwd()
# goodreadsquotes.grabber("https://www.goodreads.com/author/quotes/4114218.C_JoyBell_C_")
blather = Blather()
# blather.read('joyce.txt')
# blather.save('joyc6.pt')
blather.load(dir + '/joyc6.pt')

res = ""
while len(res) < 45 or len(res) > 250:
    res = blather.write(' ')
quoteText = '"' + res.strip() + '"'
joyceImages.make_image(f'{quoteText}')
client.make_post('generations/image.jpg', quoteText)
