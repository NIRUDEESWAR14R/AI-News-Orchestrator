from news_fetcher import fetch_articles
from event_extractor import extract_milestones_from_articles

articles = fetch_articles("India Moon Mission", 2)

events = extract_milestones_from_articles(articles)

for e in events:
    print(e.date, e.title)
    print(e.description)
    print("-----")
