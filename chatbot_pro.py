import requests
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# SCRAPE WEBSITE
# -------------------------------
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    texts = []

    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'li', 'span']):
        text = tag.get_text().strip()

        # filter garbage text
        if len(text) > 40 and not any(x in text.lower() for x in ['cookie', 'privacy', 'login']):
            texts.append(text)

    return list(set(texts))


# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text


# -------------------------------
# CHUNK DATA
# -------------------------------
def chunk_data(texts, chunk_size=2):
    chunks = []

    for i in range(0, len(texts), chunk_size):
        chunk = " ".join(texts[i:i+chunk_size])
        chunks.append(clean_text(chunk))

    return chunks


# -------------------------------
# CREATE VECTOR DB
# -------------------------------
def create_vector_db(chunks):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(chunks)
    return vectorizer, vectors


# -------------------------------
# SEARCH
# -------------------------------
def search(query, chunks, vectorizer, vectors):
    query_vec = vectorizer.transform([clean_text(query)])
    scores = cosine_similarity(query_vec, vectors).flatten()

    top_indices = scores.argsort()[-3:][::-1]

    results = [chunks[i] for i in top_indices]
    return results


# -------------------------------
# FORMAT ANSWER
# -------------------------------
def format_answer(results):
    if not results:
        return "Sorry, I couldn't find a good answer."

    # take best result only
    best = results[0]

    # clean sentence
    best = best.replace("\n", " ").strip()

    return best.capitalize()