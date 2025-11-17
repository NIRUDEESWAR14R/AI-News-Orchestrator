import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

class Article:
    def __init__(self, title, url, published_at, source_name, content):
        self.title = title
        self.url = url
        self.published_at = published_at
        self.source_name = source_name
        self.content = content

def fetch_articles(query, max_results=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "pageSize": max_results,
        "sortBy": "relevancy",
        "apiKey": NEWSAPI_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print("Error:", data)
        return []

    articles = []
    for a in data.get("articles", []):
        title = a["title"]
        url_ = a["url"]
        published_at = a.get("publishedAt")

        if published_at:
            published_at = datetime.fromisoformat(published_at.replace("Z", "+00:00"))

        source_name = a["source"]["name"]
        content = a.get("content") or a.get("description") or ""

        articles.append(Article(title, url_, published_at, source_name, content))

    return articles
