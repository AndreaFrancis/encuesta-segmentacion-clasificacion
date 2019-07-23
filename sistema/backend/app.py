from flask import Flask, request, jsonify
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    
    X = request.get_json()

    app.logger.info(X)

    clf = joblib.load('model.pkl')
    #probabilities = clf.predict_proba([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
    probabilities = clf.predict_proba([X])
    return jsonify([{'name': 'Sind. ulceroso', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Sind. dispeptico', 'value': round(probabilities[0, 1] * 100, 2)},
                    {'name': 'Sind. ansioso', 'value': round(probabilities[0, 2] * 100, 2)},
                    {'name': 'Rectorragia', 'value': round(probabilities[0, 3] * 100, 2)},
                    {'name': 'Paracitosis', 'value': round(probabilities[0, 4] * 100, 2)},
                    {'name': 'Hepatopatia', 'value': round(probabilities[0, 5] * 100, 2)},
                    {'name': 'Gastroenteritis', 'value': round(probabilities[0, 6] * 100, 2)},
                    {'name': 'Estrenimiento', 'value': round(probabilities[0, 7] * 100, 2)},
                    {'name': 'Erge', 'value': round(probabilities[0, 8] * 100, 2)},
                    {'name': 'Dolor abdominal', 'value': round(probabilities[0, 9] * 100, 2)},
                    {'name': 'Dispepsia', 'value': round(probabilities[0, 10] * 100, 2)},
                    {'name': 'Diarrea cronica', 'value': round(probabilities[0, 11] * 100, 2)},
                    {'name': 'Colelitiasis', 'value': round(probabilities[0, 12] * 100, 2)}])


@app.route('/api/predict1', methods=['POST'])
def predict_illnes():
    clf = joblib.load('nn.pkl')

    X = [[0.67032967, 
    0.213419784,
    0.288936312,
    0.158501441,
    0.658396719,
    0.510638298,
    1,
    0.243607014,
    0,
    0.28981974,
    0.595959644,
    0.330083565,
    0.72826087,
    0.289855072,
    0.214285714,
    0.367346939]]
    probabilities = clf.predict_proba(X)
    return jsonify([{'name': 'Infeccion del tracto urinario', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Dolor abdominal', 'value': round(probabilities[0, 1] * 100, 2)},
                    {'name': 'Pancreatitis', 'value': round(probabilities[0, 2] * 100, 2)},
                    {'name': 'Hemorragia digestiva', 'value': round(probabilities[0, 3] * 100, 2)}])
if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
