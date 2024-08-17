from src import create_app
from src.config import Config, PORT
from gevent import pywsgi

app = create_app(Config)

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', PORT), app)
    server.serve_forever()
    app.run()
