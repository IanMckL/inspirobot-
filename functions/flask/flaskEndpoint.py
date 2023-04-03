from flask import Flask, request
from threading import Thread
from pyngrok import ngrok
from functions.instagram import client as ig


def init_flask():
    app = Flask(__name__)
    ngrok_public_url = ngrok.connect(5003)
    print(ngrok_public_url)
    data = "Henlo"

    @app.route('/', methods=['POST'])
    def verify():

        field = request.json["entry"][0]["changes"][0]["field"]
        value = request.json["entry"][0]["changes"][0]["value"]

        if field == "comments":
            media_id = request.json["entry"][0]["changes"][0]["value"]["media"]["id"]
            user_id = request.json["entry"][0]["changes"][0]["value"]["from"]["id"]
            comment_id = value["id"]
            username = request.json["entry"][0]["changes"][0]["value"]["from"]["username"]
            comment = value["text"]

            ig.respond_to_comment(media_id, comment_id, username, "Write me a poem about morning")
            print("a new comment has been made", value["text"])

        if field == "mentions":
            print("Ooh! Someone mentioned me! Better respond")
        return '', 200

    @app.route('/', methods=['GET'])
    def webhook():
        challenge = request.args.get('hub.challenge')
        print('challenge', challenge)
        return challenge, 200

    def flaskthread():
        print("in flaskthread")
        app.run(port=5003)

    # create and start thread to run Flask app
    t = Thread(target=flaskthread)
    t.start()

    # return Flask app object
    return app
