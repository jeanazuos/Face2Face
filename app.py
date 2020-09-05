import os
from flask import Flask
from flask-swagger-ui import get_swaggerui_blueprint

from views.views import my_bp

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH'))
app.register_blueprint(my_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)