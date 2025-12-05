import re
import heapq
from collections import Counter

def generate_title(text):
    """ Take most frequent meaningful word and create auto-title """
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    commons = Counter(words).most_common(1)
    if commons:
        return f"Summary About {commons[0][0].title()}"
    return "AI Generated Summary"


def extract_keywords(text, limit=5):
    """ Extract top 5 keywords """
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    freq = Counter(words)
    common = [w.title() for w, _ in freq.most_common(limit)]
    return common


def ai_summarizer(text, mode="medium"):
    if not text:
        return ""

    clean = re.sub(r'\s+', ' ', text)

    sentences = re.split(r'(?<=[.!?]) +', clean)
    sentences = [s.strip() for s in sentences if s.strip()]

    # MODE SETTINGS
    if mode == "short":
        max_sent = 2
    elif mode == "detailed":
        max_sent = 6
    else:
        max_sent = 3

    # FREQUENCY TABLE
    formatted = re.sub('[^a-zA-Z]', ' ', clean)
    words = formatted.lower().split()
    stop = {'the', 'is', 'in', 'and', 'to', 'of', 'for', 'with'}
    freq = {}

    for w in words:
        if w not in stop:
            freq[w] = freq.get(w, 0) + 1

    if not freq:
        return text

    max_f = max(freq.values())
    for w in freq:
        freq[w] /= max_f

    score = {}
    for sent in sentences:
        for word in sent.lower().split():
            if word in freq:
                score[sent] = score.get(sent, 0) + freq[word]

    # PICK TOP SENTENCES
    best = heapq.nlargest(max_sent, score, key=score.get)

    # RETURN BULLET FORMAT
    return "\n• " + "\n• ".join(best)
