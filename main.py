from flask import Flask
from flask_cors import CORS
import os
from routes.diagnosis_routes import ruta


app = Flask(__name__)

app.register_blueprint(ruta)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    # app.run(debug=True)