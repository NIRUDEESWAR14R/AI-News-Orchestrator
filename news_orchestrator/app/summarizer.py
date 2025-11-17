from transformers import pipeline

# Fast CPU-friendly model
summ_model = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

class EventSummary:
    def __init__(self, overview, highlights, discrepancies):
        self.overview = overview
        self.highlights = highlights
        self.discrepancies = discrepancies

def build_event_summary(query, timeline, articles):
    # Convert timeline to readable text
    timeline_text = ""
    for m in timeline:
        date_str = m.date.strftime("%Y-%m-%d") if m.date else "Unknown"
        timeline_text += f"{date_str}: {m.description} "

    # Generate summary paragraph
    overview = summ_model(
        timeline_text,
        max_length=120,
        min_length=40,
        do_sample=False
    )[0]["summary_text"]

    # Generate simple highlights (top 3)
    highlights = []
    for m in timeline[:3]:
        highlights.append(f"{m.title} — {m.description[:80]}...")

    # Local models cannot detect discrepancies well, so placeholder
    discrepancies = ["Local model cannot detect discrepancies between sources."]

    return EventSummary(overview, highlights, discrepancies)
