from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Your NewsAPI Key (replace 'your_api_key' with your actual key)
API_KEY = '1c5d52c314c14c8ab03f53ff33bf7429'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

# Fetch the latest headlines for all countries, sorted by date (latest)
def get_news(sort_by="publishedAt"):
    """Fetch news from NewsAPI sorted by the given parameter (default: latest)"""
    params = {
        'apiKey': API_KEY,
        'sortBy': sort_by,  # Sort by latest news
    }
    response = requests.get(NEWS_API_URL, params=params)
    return response.json()

@app.route('/')
def index():
    """Home route to display news headlines"""
    news = get_news()
    return render_template('index.html', articles=news.get('articles', []))

@app.route('/search', methods=['GET'])
def search():
    """Search route to filter news based on user input"""
    query = request.args.get('query', '')
    if query:
        params = {
            'q': query,
            'apiKey': API_KEY,
        }
        response = requests.get(f'https://newsapi.org/v2/everything', params=params)
        news = response.json()
        return render_template('index.html', articles=news.get('articles', []))
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
