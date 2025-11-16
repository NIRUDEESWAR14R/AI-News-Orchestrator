# 📰 AI News Orchestrator (Local LLM Powered)
### Reconstructing the story behind the headlines — Fully Offline, Fast & Free

The **AI News Orchestrator** is an end-to-end intelligent system that takes a news topic (e.g., *“Venus spacecraft crash”*, *“Chandrayaan-3 landing”*, *“COP28 updates”*), fetches real articles from multiple sources, extracts the key events, generates a chronological timeline, and produces a clean summary — all powered by **local machine learning models**.

No API costs.  
No quotas.  
No OpenAI/Gemini keys.  
Works completely offline!

---

## 🚀 Features

### **📰 Multi-source Article Aggregation**
- Fetches top news articles related to the input topic  
- Extracts title, publication date, source, and content

### **🧠 Local AI Event Extraction**
Powered by HuggingFace `distilbart-cnn-12-6`:
- Extracts 3–6 key milestones from each article  
- Identifies dates, titles, and descriptions  
- Works without any API calls  

### **📆 Timeline Reconstruction**
- Merges milestones from all articles  
- Sorts chronologically  
- Groups similar events  
- Produces a clean event timeline

### **📝 Summary Generation**
Local summarizer produces:
- Overview paragraph  
- Key highlights  
- Notes on source differences

### **🖥️ Streamlit UI**
A modern, clean user interface that displays:
- Timeline  
- Summary  
- Highlights  
- Sources and links  

All in a two-column layout.

---

## 🏗️ Architecture Overview

User Query → News Fetcher → Local AI Event Extractor
→ Timeline Builder → Summary Generator → Streamlit UI

### **Modules**
| Module | Description |
|--------|-------------|
| `news_fetcher.py` | Fetches news using NewsAPI |
| `event_extractor.py` | Summarizes articles into milestones using local LLM |
| `timeline_builder.py` | Builds chronological event timeline |
| `summarizer.py` | Creates overall summary + highlights |
| `main.py` | Streamlit web interface |

---

## 🛠️ Installation

### 1. Clone / Download


git clone <repo-url>
cd news_orchestrator


### 2. Create Virtual Environment


python -m venv env
env\Scripts\activate # Windows
source env/bin/activate # Mac/Linux


### 3. Install Dependencies


pip install -r requirements.txt
python -m spacy download en_core_web_sm


### 4. Run App


streamlit run app/main.py


---

## 🧪 Example Use Cases

- Track major space missions  
- Understand political events  
- Summarize global conferences  
- Combine multiple news sources into a single truth  
- Research timelines for projects, dissertations, or reports  

---

## 📚 Tech Stack

- **Python 3.8+**
- **Streamlit** (Frontend)
- **HuggingFace Transformers** (Local LLM)
- **DistilBART CNN** (Summarization)
- **NewsAPI** (Article fetching)
- **DateParser** (Date detection)

---

## ✨ Why This Project Stands Out

- 100% offline NLP  
- Clean & professional UI  
- Doesn’t depend on expensive APIs  
- Reconstructs news evolution over time  
- Perfect for portfolios, hackathons, and academic submissions  

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to suggest improvements or new features.

---

## 📄 License

MIT License © 2025
