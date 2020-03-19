from flask import Flask
from flask_cors import CORS
from flask import jsonify
from services.get_data import get_data
from services.get_helpline_numbers import helpline_numbers

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('settings/settings.py')

@app.route('/data')
def data():
    data = get_data()

    return jsonify({
        'India_coronavirus': data,
        'disclaimer': "This data is provided to the public strictly for educational and academic research purposes. The API relies upon publicly available data from multiple sources, that do not always agree. We hereby disclaim any and all representations and warranties with respect to the API, including accuracy, fitness for use, and merchantability. Reliance on the API for medical guidance or use of the API in commerce is strictly prohibited.",
        'central_helpline': "+91-11-23978046"
    })

@app.route('/')
def helplines():
    return jsonify({
        'helplines': helpline_numbers(),
        'disclaimer': "Please refer this link for updated helpline numbers https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf. This data is provided to the public strictly for educational and academic research purposes. The API relies upon publicly available data from multiple sources, that do not always agree. We hereby disclaim any and all representations and warranties with respect to the API, including accuracy, fitness for use, and merchantability. Reliance on the API for medical guidance or use of the API in commerce is strictly prohibited.",
        'central_helpline': "+91-11-23978046"
    })

if __name__ == '__main__':
    app.run()