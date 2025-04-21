import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume(resume_text):
    conn = sqlite3.connect("app/jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()

    vectorizer = CountVectorizer().fit_transform([resume_text] + [job[0] + " " + job[1] + " " + job[2] for job in jobs])
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity([vectors[0]], vectors[1:])
    scores = cosine_matrix[0]
    
    ranked_jobs = sorted(zip(jobs, scores), key=lambda x: x[1], reverse=True)
    return ranked_jobs[:10]
