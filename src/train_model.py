from sklearn.ensemble import IsolationForest
import joblib
from preprocess import vectorize_text
from read_logs import read_log_file

def train(contamination=0.2):
    df = read_log_file()
    X, vectorizer = vectorize_text(df['message'], max_features=50)
    
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X.toarray())
    
    joblib.dump(model, 'isolation_forest_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

    return model    
if __name__ == "__main__":
    model = train()
    print("Model trained and saved.")