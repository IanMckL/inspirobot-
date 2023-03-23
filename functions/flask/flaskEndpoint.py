from flask import Flask, request, jsonify
from pyngrok import ngrok
def init_flask():
    app = Flask(__name__)
    ngrokPublicUrl = ngrok.connect(5003)
    print(ngrokPublicUrl)

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

    app.run(port=5003)
