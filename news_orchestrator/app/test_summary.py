from news_fetcher import fetch_articles
from event_extractor import extract_milestones_from_articles
from timeline_builder import build_timeline
from summarizer import build_event_summary

articles = fetch_articles("Venus spacecraft", 3)
events = extract_milestones_from_articles(articles)
timeline = build_timeline(events)
summary = build_event_summary("Venus spacecraft", timeline, articles)

print("\n--- OVERVIEW ---\n")
print(summary.overview)

print("\n--- HIGHLIGHTS ---")
for h in summary.highlights:
    print("-", h)

print("\n--- DISCREPANCIES ---")
for d in summary.discrepancies:
    print("-", d)
