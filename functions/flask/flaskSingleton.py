from functions.flask.flaskEndpoint import init_flask


class FlaskApp:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if FlaskApp.__instance is None:
            FlaskApp.__instance = super(FlaskApp, cls).__new__(cls)
            FlaskApp.__instance.init_flask_app()
        return FlaskApp.__instance

    def init_flask_app(self):
        self.app = init_flask()

