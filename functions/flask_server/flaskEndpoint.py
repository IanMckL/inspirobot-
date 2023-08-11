from threading import Thread

from flask import Flask, request, Markup
from pyngrok import ngrok


def init_flask():
    app = Flask(__name__)
    ngrok_public_url = ngrok.connect(5003)
    print(ngrok_public_url)
    data = "Henlo"

    @app.route("/")
    def main():
        return data




    @app.route('/', methods=['POST'])
    def verify():

        field = request.json["entry"][0]["changes"][0]["field"]
        value = request.json["entry"][0]["changes"][0]["value"]

        if field == "comments":
            print("a new comment has been made")

        if field == "mentions":
            print("Ooh! Someone mentioned me! Better respond")
        return '', 200

    @app.route('/', methods=['GET'])
    def webhook():
        challenge = request.args.get('hub.challenge')
        return challenge, 200

    def flaskthread():
        print("in flaskthread")
        app.run(port=5003)

        # create and start thread to run Flask app
    t = Thread(target=flaskthread)
    t.start()
        # return Flask app object
    return app


