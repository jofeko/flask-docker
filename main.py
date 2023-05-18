from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/random_quote')
def get_random_quote():
    api_url = 'https://api.quotable.io/random'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        quote = response.json()
        return jsonify({'quote': quote['content'], 'author': quote['author']})
    else:
        return jsonify({'error': 'Failed to retrieve a random quote.'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
