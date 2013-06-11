import logging, sys
from flaskbp.application import create_app

logging.basicConfig(stream=sys.stderr)

app = create_app()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug = True)