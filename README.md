🤖 AI Chatbot – Web-Based Intelligent Assistant

📌 Overview

This project is a web-based chatbot application designed to provide intelligent responses by extracting and processing relevant information from a given website. The system combines web scraping and Natural Language Processing (NLP) techniques to simulate an AI-powered conversational assistant.

---

🚀 Features

- 🌐 Scrapes real-time data from a website
- 🧠 Uses NLP (TF-IDF + Cosine Similarity) for intelligent response retrieval
- 💬 Interactive chat interface with smooth UI
- ⚡ Fast and lightweight backend using Flask
- 🎯 Context-based answer generation from knowledge base

---

🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- NLP: Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- Web Scraping: BeautifulSoup, Requests

---

⚙️ How It Works

1. The system scrapes textual data from the target website.
2. Data is cleaned and divided into smaller chunks.
3. TF-IDF vectorization converts text into numerical form.
4. User query is compared using cosine similarity.
5. The most relevant content is returned as a response.

---

🧪 Example Queries

- What is BotPenguin?
- Pricing details
- Features of the chatbot

---

🔮 AI Enhancement (Optional)

This project is designed with extensibility in mind. It can be integrated with advanced AI models (such as GPT-based APIs) to enhance conversational intelligence, context understanding, and response generation.

«Note: API-based AI integration can be enabled for improved performance and more human-like responses.»

---

📂 Project Structure

chatbot_submission_final/
│
├── app.py
├── chatbot_pro.py
├── templates/
│   └── index.html
└── README.md

---

▶️ How to Run

1. Install dependencies:

pip install flask requests beautifulsoup4 scikit-learn

2. Run the application:

python app.py

3. Open in browser:

http://127.0.0.1:5000

---

💡 Future Improvements

- Integration with GPT / LLM APIs
- Voice-based interaction
- Chat history & memory
- Deployment on cloud platforms

---

📌 Conclusion

This project demonstrates how NLP techniques can be used to build an intelligent chatbot capable of retrieving meaningful information from web data, with the flexibility to scale into a full AI-powered assistant.

---