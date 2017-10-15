from flask import Flask

app = Flask(__name__)

import wiredbraincoffee.views  # NOQA

if __name__ == '__main__':
    app.run()
