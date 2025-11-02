# 🧠 AI-Powered Log Anomaly Detection (SRE Project)

## 📘 Overview
This project is designed to help **Site Reliability Engineers (SREs)** automatically detect anomalies in application logs using **Machine Learning**.  
It processes system or application logs, identifies unusual patterns, and highlights potential **errors, timeouts, or performance issues** — assisting in faster incident response and proactive reliability management.

---

## 🚀 Problem Statement
Modern production systems generate millions of log lines daily.  
Manually identifying issues is time-consuming and error-prone.  
This project automates the process by using AI to **detect abnormal log behavior in real time**.

**Goal:** Build an ML-based system that continuously monitors logs and flags unusual events before they cause outages.

---

## 🏗️ Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3.11+** | Core programming language |
| **scikit-learn (Isolation Forest)** | Unsupervised anomaly detection |
| **TF-IDF Vectorizer** | Text feature extraction from logs |
| **Streamlit** | Interactive web dashboard for visualization |
| **Pandas / NumPy** | Data processing |
| **Docker SDK / Kubernetes API** | (Optional) Fetch live container or pod logs |
| **Joblib** | Model and vectorizer persistence |

---


---

## 🧩 How It Works

1. **Preprocessing:**  
   - Converts raw log messages into numerical vectors using **TF-IDF**.  
   - Each message is represented as a feature vector.

2. **Modeling:**  
   - Uses **Isolation Forest** to learn what “normal” log behavior looks like.  
   - Flags deviations as anomalies (`-1`).

3. **Visualization:**  
   - A **Streamlit dashboard** displays logs, anomaly counts, and severity levels.

4. **(Optional)**:  
   - Stream live logs from **Docker** or **Kubernetes pods**.  
   - Detect anomalies in real-time.

---

## 🧠 Example Usage

### Train and Save Model
```bash
python src/train_model.py

Future Improvements

Use sentence-transformers embeddings instead of TF-IDF for richer semantic understanding.

Stream live Docker/Kubernetes logs using the Docker SDK or K8s Python API.

Send Slack/email alerts when anomalies are detected.

Use ensemble models (Isolation Forest + statistical z-score) to reduce false positives.

Add unit tests for data preprocessing and model accuracy.

💡 Real-World Impact

This project showcases how AI and SRE practices can blend to automate reliability monitoring.
By implementing anomaly detection on log streams, SREs can:

Catch issues earlier

Reduce downtime

Improve incident response time

🧑‍💻 Author

Priya Bellad
Munich, Germany
Data Analyst | SRE | Machine Learning Enthusiast
📫 LinkedIn Profile
 (Add your link here)
