from blather import Blather
from functions.joyImageGen import joyceImages

# goodreadsquotes.grabber("https://www.goodreads.com/author/quotes/4114218.C_JoyBell_C_")
blather = Blather()
# blather.read('joyce.txt')
# blather.save('joyc4.pt')
blather.load('./models/joyc4.pt')

res = ""

while len(res) <10 or len(res) > 250:
    res = blather.write(' ')

joyceImages.make_image(f'{res}')
print(f'C JoyBot Says: {res}')
