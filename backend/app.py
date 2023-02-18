from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from random import random
from Clases.PeticionError import *

HOST = '0.0.0.0'
PORT = 8081


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        X = request.get_json()
        res = float(X['numero']) * random()
        return jsonify({'response': res})
    except:
        raise PeticionError(message = 'Peticion Mal Formateada', status_code = 400)

@app.errorhandler(PeticionError)
def handle_peticion_mal_formateada(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run(host=HOST, debug=True, port=PORT)