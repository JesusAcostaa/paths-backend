from flask import Flask
from flask_cors import CORS
import os
from routes.diagnosis_routes import ruta


app = Flask(__name__)

app.register_blueprint(ruta)
CORS(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)