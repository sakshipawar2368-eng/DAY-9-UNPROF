# DAY-9-UNPROF
# 📝 NLP Text Analyzer

## 📌 Project Description

This project is a simple **Natural Language Processing (NLP) Text Analyzer** developed using **Python**, **NLTK**, and **Matplotlib**. It analyzes a text article by performing basic NLP preprocessing techniques and displays the most frequently occurring words.

---

## 🚀 Features

- Performs **Tokenization** using Regular Expressions (`re`)
- Removes **English Stopwords**
- Applies **Stemming** using Porter Stemmer
- Applies **Lemmatization** using WordNet Lemmatizer
- Extracts the **Top 10 Most Frequent Keywords**
- Displays a **Bar Chart** of keyword frequencies

---

## 🛠️ Technologies Used

- Python
- NLTK
- Matplotlib
- Regular Expressions (`re`)
- Collections (`Counter`)

---

## 📚 Python Libraries

```python
re
collections
matplotlib
nltk
```

---

## ▶️ How to Run

1. Install the required libraries:

```bash
pip install nltk matplotlib
```

2. Download the required NLTK datasets (only the first time):

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

3. Open the Python file or Jupyter Notebook.

4. Run the program.

---

## 📊 Output

The program displays:

- Total number of tokens
- Words after stopword removal
- Sample stemmed words
- Sample lemmatized words
- Top 10 most frequent keywords
- Bar chart of keyword frequencies

---

## 📂 Project Structure

```
Day9_NLP_Text_Analyzer/
│
├── text_analyzer.ipynb
├── README.md
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Tokenization
- Stopword Removal
- Stemming
- Lemmatization
- Keyword Extraction
- Word Frequency Analysis
- Data Visualization using Matplotlib

---

