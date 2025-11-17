import streamlit as st

from news_fetcher import fetch_articles
from event_extractor import extract_milestones_from_articles
from timeline_builder import build_timeline
from summarizer import build_event_summary

# App settings
st.set_page_config(
    page_title="AI News Orchestrator",
    layout="wide"
)

st.title("📰 AI-Powered News Orchestrator (Local Version)")
st.write("Summarize events, build timelines, and understand a news story — all locally, with zero API calls!")

query = st.text_input("Enter a news topic or event:", placeholder="e.g., Venus spacecraft, Chandrayaan-3, COP28 Summit")

if st.button("Analyze"):
    if not query.strip():
        st.warning("Please enter a topic before analyzing.")
    else:
        with st.spinner("Collecting news and analyzing events..."):
            
            # STEP 1: Fetch articles
            articles = fetch_articles(query, max_results=5)

            if not articles:
                st.error("No articles found. Try a different topic.")
                st.stop()

            # STEP 2: Extract milestones
            milestones = extract_milestones_from_articles(articles)

            # STEP 3: Build timeline
            timeline = build_timeline(milestones)

            # STEP 4: Summarize
            summary = build_event_summary(query, timeline, articles)

        st.success("Analysis complete!")

        # Layout
        col1, col2 = st.columns([2, 1])

        # -----------------------------------------------
        # LEFT SIDE — TIMELINE + SUMMARY
        # -----------------------------------------------
        with col1:
            st.header("📆 Timeline of Events")

            for m in timeline:
                date_str = m.date.strftime("%Y-%m-%d") if m.date else "Unknown"
                st.subheader(f"{date_str} — {m.title}")
                st.write(m.description)
                st.caption("Sources: " + ", ".join(m.sources))
                st.markdown("---")

            st.header("📝 Event Summary")
            st.write(summary.overview)

            st.header("⭐ Key Highlights")
            for h in summary.highlights:
                st.markdown(f"- {h}")

        # -----------------------------------------------
        # RIGHT SIDE — SOURCE INFO
        # -----------------------------------------------
        with col2:
            st.header("📚 Articles Used")
            for a in articles:
                st.markdown(f"**{a.source_name}**")
                st.write(a.title)
                st.caption(a.url)
                st.markdown("---")

            st.header("⚠️ Source Differences")
            for d in summary.discrepancies:
                st.markdown(f"- {d}")
