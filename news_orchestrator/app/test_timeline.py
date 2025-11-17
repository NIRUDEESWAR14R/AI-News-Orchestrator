from news_fetcher import fetch_articles
from event_extractor import extract_milestones_from_articles
from timeline_builder import build_timeline

articles = fetch_articles("Venus spacecraft", 3)
events = extract_milestones_from_articles(articles)
timeline = build_timeline(events)

for e in timeline:
    print(e.date, "|", e.title)
    print(e.description)
    print("Sources:", e.sources)
    print("-----")
