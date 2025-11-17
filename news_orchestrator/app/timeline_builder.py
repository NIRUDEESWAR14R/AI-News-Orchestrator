from datetime import datetime
from event_extractor import EventMilestone

def build_timeline(milestones):
    # Sort by date, unknown dates go last
    def sort_key(m):
        return m.date if m.date else datetime.max

    milestones = sorted(milestones, key=sort_key)

    # Merge events happening on same day
    merged = []
    seen_dates = {}

    for m in milestones:
        date_key = m.date.strftime("%Y-%m-%d") if m.date else "Unknown"

        if date_key not in seen_dates:
            merged.append(
                EventMilestone(
                    date=m.date,
                    title=m.title,
                    description=m.description,
                    sources=m.sources
                )
            )
            seen_dates[date_key] = len(merged) - 1
        else:
            existing = merged[seen_dates[date_key]]
            existing.description += " " + m.description
            existing.sources = list(set(existing.sources + m.sources))

    return merged
