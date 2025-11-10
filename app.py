from flask import Flask, render_template, request, redirect, url_for
import requests
from config import NEWS_API_KEY



#CREATE FLASK APP
app = Flask(__name__)




#HOME ROUTE
@app.route('/')
def index():
    query = request.args.get('query','latest')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_news = response.json()
    articles = news_news.get('articles', [])
   # print(news_news)  # Debugging line to check the fetched articles

    
    return render_template('index.html', articles=articles, query=query)







if __name__ == '__main__':
    app.run(debug=True) 

# Run the Flask app in debug mode