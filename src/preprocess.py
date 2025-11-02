from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


def vectorize_text(text_series, max_features=100):
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(text_series)
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    return X, vectorizer


# ⚠️ Everything below runs only when you execute THIS file directly,
# not when you import it from another script.
if __name__ == "__main__":
    from read_logs import read_log_file

    df = read_log_file()
    X, vectorizer = vectorize_text(df['message'], max_features=50)

    # ✅ All print statements INSIDE the main block
    print("X is ", X)
    print("Vectorizer is ", vectorizer)
    print("TF-IDF feature matrix shape:", X.shape)
    print("Number of features:", len(vectorizer.get_feature_names_out()))

