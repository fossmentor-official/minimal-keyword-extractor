import re     # regular expressions module, used for text cleaning
import math   # math module, used for idf calculation
from collections import Counter # Counter module, used for counting words

# Minimal stopwords list (can expand later)
STOPWORDS = set("""
a about above after again against all am an and any are aren't as at be because been before being below
between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each
few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers
herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me
more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over
own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs
them themselves then there there's these they they'd they'll they're they've this those through to too under
until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which
while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself
yourselves
""".split())

def clean_text(text): # cleans the text by converting it to lowercase and removing non-alphanumeric characters
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

# Minimal sentence splitter
def tokenize_sentences(text):
    sentences = text.split('.')  # Split by periods
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

# Minimal word tokenizer
def tokenize_words(text): # tokenizes the text by splitting it into words and removing stopwords
    words = text.split()
    return [w for w in words if w.isalpha() and w not in STOPWORDS]

def compute_tf(doc_words):
    total_words = len(doc_words)
    word_counts = Counter(doc_words)
    return {word: count / total_words for word, count in word_counts.items()}

def compute_idf(docs): # computes the idf score for each word in the document
    N = len(docs)
    idf = {}
    all_words = set(word for doc in docs for word in doc)
    for word in all_words:
        containing = sum(1 for doc in docs if word in doc)
        idf[word] = math.log((1 + N) / (1 + containing)) + 1
    return idf

def compute_tfidf(docs): # computes the tf-idf score for each word in the document
    idf = compute_idf(docs)
    doc_tfidf = []
    for doc in docs:
        tf = compute_tf(doc)
        tfidf = {word: tf[word] * idf[word] for word in doc}
        doc_tfidf.append(tfidf)
    return doc_tfidf

def extract_keywords(text, top_k=10): # extracts the top k keywords from the text
    text = clean_text(text)
    sentences = tokenize_sentences(text)
    docs = [tokenize_words(sent) for sent in sentences]
    tfidf_scores = compute_tfidf(docs)
    combined = Counter()
    for tfidf in tfidf_scores:
        combined.update(tfidf)
    return combined.most_common(top_k)

if __name__ == "__main__":
    with open("data/sample_text.txt") as f: # reads the sample text from the file
        sample_text = f.read()
    keywords = extract_keywords(sample_text, top_k=10) # extracts the top 10 keywords from the sample text
    print("Top Keywords:")
    for word, score in keywords:
        print(f"{word}: {round(score, 4)}") # prints the keywords and their scores
