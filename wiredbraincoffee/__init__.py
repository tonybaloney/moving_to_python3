try:
    from flask import Flask

    app = Flask(__name__)
except ImportError:
    import warnings
    warnings.warn("Cannot import Flask")
    app = None

import wiredbraincoffee.views  # NOQA

if __name__ == '__main__':
    app.run()
