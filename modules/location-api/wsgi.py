import os
import logging
import sys

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    # set logger to handle STDOUT and format output
    stdout_handler = logging.StreamHandler(sys.stdout)
    format_output = '%(asctime)s %(message)s'

    logging.basicConfig(format=format_output, level=logging.DEBUG, handlers=[stdout_handler])

    logger = logging.getLogger("name")
    h2 = logging.StreamHandler(sys.stderr)
    h2.setLevel(logging.ERROR)
    logger.addHandler(h2)
    app.run(debug=True)
