from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = '3015e05721af4c649ee3a79cafb5488c'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news', methods=['GET'])
def news():
    country = request.args.get('country', 'us')
    params = {
        'apiKey': API_KEY,
        'country': country
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from API'}), 500

    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
