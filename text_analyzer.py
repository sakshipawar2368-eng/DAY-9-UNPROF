import re
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer



text = """
Artificial Intelligence (AI) is transforming industries around the world.
It is used in healthcare, education, agriculture, banking, transportation,
and many other sectors. AI enables machines to learn from data, recognize
patterns, make decisions, and solve complex problems. Machine learning,
deep learning, and natural language processing are important branches of AI.

Natural Language Processing allows computers to understand human language.
Applications include chatbots, virtual assistants, language translation,
spam detection, sentiment analysis, speech recognition, and text
summarization.

Python is one of the most popular programming languages for AI because it
has powerful libraries such as NumPy, Pandas, Matplotlib, Scikit-learn,
TensorFlow, PyTorch, and NLTK. Developers use these libraries to analyze
data, build machine learning models, visualize results, and process text.

Students who learn Python and NLP can build interesting projects such as
resume screening systems, fake news detection, email spam classifiers,
question answering systems, document summarizers, recommendation systems,
and intelligent chatbots.

Data preprocessing is one of the most important steps in NLP. It includes
tokenization, stopword removal, stemming, lemmatization, and keyword
extraction. These techniques help clean text before machine learning models
are trained.

The future of AI looks promising. Businesses are investing heavily in AI
solutions to automate tasks and improve customer experience. Researchers
continue to develop better algorithms that make AI systems more accurate,
efficient, and reliable. Learning NLP today opens the door to many exciting
career opportunities in data science, machine learning, and artificial
intelligence.
"""

# Tokenization using regex (No punkt required)
tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in tokens if word not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Count word frequency
word_freq = Counter(lemmatized_words)

# Top 10 keywords
top10 = word_freq.most_common(10)

# Output
print("="*50)
print("NLP TEXT ANALYZER")
print("="*50)

print("\nTotal Tokens:", len(tokens))
print("Words After Stopword Removal:", len(filtered_words))

print("\nFirst 20 Tokens:")
print(tokens[:20])

print("\nFirst 20 Stemmed Words:")
print(stemmed_words[:20])

print("\nFirst 20 Lemmatized Words:")
print(lemmatized_words[:20])

print("\nTop 10 Keywords:")
for word, count in top10:
    print(f"{word}: {count}")

# Plot graph
words = [w for w, c in top10]
counts = [c for w, c in top10]

plt.figure(figsize=(10,5))
plt.bar(words, counts)
plt.title("Top 10 Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()

print("\nProject Completed Successfully!")
