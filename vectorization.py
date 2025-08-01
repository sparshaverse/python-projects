from sklearn.feature_extraction.text import TfidfVectorizer


corpus = [
    "Data Science is fun"
    "Python makes data science easy"
    "Machine learning is a part of data science"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())