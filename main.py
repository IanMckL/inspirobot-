import datetime
import os
import sys

from functions.flask_server.flaskEndpoint import init_flask
from functions.instagram import client
from functions.joyImageGen import joyceImages
from functions.joyceScraper import goodreadsquotes
from functions.parroty.parroty import Parroty
directory = os.getcwd()
parroty = Parroty()

# if args are passed in, use them
if len(sys.argv) > 1:
    argument = sys.argv[1]
    if argument == 'build':
        print('Building model...')
        parroty.create_model(directory + '/joybell_comments.txt')
        parroty.save_model(directory + '/models/joybell_comments.pt')
    elif argument == 'make-post':
        print('Making post...')
        parroty.load_model(directory + '/models/joyc7.pt')
        res = parroty.generate_text_from_model(' ')
        quoteText = '"' + res.strip() + '"'
        print(quoteText)
        joyceImages.make_image(f'{quoteText}')
        client.make_post('generations/image.jpg', quoteText)
    elif argument == 'joy-routine':
        client.joy_routine()
        print('scan')
    elif argument == 'random-comment':
        client.create_random_comment()
        print('test')
    elif argument == 'flask_server':
        print('flask_server')
        flaskapp = init_flask()
        app = flaskapp.app
        @app.route('/flaskargs', methods=['GET'])
        def flaskargs():
            return 'Joybot is here and she is queer!'





# goodreadsquotes.grabber("https://www.goodreads.com/author/quotes/4114218.C_JoyBell_C_")

# print(f'Posted to Instagram at {datetime.datetime.now()}')
