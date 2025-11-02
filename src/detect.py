import joblib
import pandas as pd
from read_logs import read_log_file


def detect(threshold_percentile=0.2):
    df = read_log_file()
    model = joblib.load('isolation_forest_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
    X = vectorizer.transform(df['message'])
    
    # Predictions: 1 = normal, -1 = anomaly
    predictions = model.predict(X.toarray())
    df['anomaly'] = predictions
    
    # Continuous anomaly scores
    scores = model.decision_function(X.toarray())
    df['anomaly_score'] = scores
    
    print("Score range:", scores.min(), scores.max())
    
    # Flag anomalies based on lowest X percentile
    threshold = df['anomaly_score'].quantile(threshold_percentile)
    anomalies = df[df['anomaly_score'] < threshold]
    
    return anomalies

if __name__ == "__main__":
    anomalies = detect()
    print("Anomalies detected:", len(anomalies))
    print(anomalies[['timestamp', 'log_level', 'message']])