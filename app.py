from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = '3015e05721af4c649ee3a79cafb5488c'  # Replace with your News API key

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch news articles
@app.route('/news')
def get_news():
    api_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'us',  # Default to US, change as needed
        'pageSize': 20  # Adjust page size as needed
    }

    # Check if query parameter 'q' is present (for search)
    query = request.args.get('q')
    if query:
        params['q'] = query

    response = requests.get(api_url, params=params)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)