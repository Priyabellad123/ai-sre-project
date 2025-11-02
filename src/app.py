
import os
import joblib


import streamlit as st
import joblib
from read_logs import read_log_file

st.title("Log Anomaly Demo")
df = read_log_file()


vec = joblib.load("src/tfidf_vectorizer.pkl")
model = joblib.load("src/isolation_forest_model.pkl")

X = vec.transform(df["message"])
df["anomaly"] = model.predict(X.toarray())
st.dataframe(df[df["anomaly"]==-1])
