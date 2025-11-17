from transformers import pipeline
from dateparser import parse as parse_date

# Fast lightweight model
extract_model = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

class EventMilestone:
    def __init__(self, date, title, description, sources):
        self.date = date
        self.title = title
        self.description = description
        self.sources = sources


def extract_milestones_from_article(article):
    # Summarize article into 3–5 bullet points
    summary = extract_model(
        article.content,
        max_length=150,
        min_length=60,
        do_sample=False
    )[0]["summary_text"]

    # Split summary into 3–6 lines
    lines = [l.strip() for l in summary.split(".") if l.strip()][:6]

    milestones = []
    for line in lines:
        # Extract date if present
        parsed_date = parse_date(line)  # may return None

        title = line[:40]  # first few words
        desc = line

        milestones.append(
            EventMilestone(
                date=parsed_date,
                title=title,
                description=desc,
                sources=[article.source_name]
            )
        )

    return milestones


def extract_milestones_from_articles(articles):
    all_events = []
    for art in articles:
        try:
            events = extract_milestones_from_article(art)
            all_events.extend(events)
        except Exception as e:
            print("Error with:", art.title, e)
    return all_events
