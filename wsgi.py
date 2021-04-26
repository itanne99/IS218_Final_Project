#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/FlaskApp/")

from main_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
