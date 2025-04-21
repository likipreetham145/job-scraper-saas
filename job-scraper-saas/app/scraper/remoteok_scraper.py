import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_and_store_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    for tr in soup.find_all("tr", class_="job"):
        job = {
            "title": tr.get("data-position"),
            "company": tr.get("data-company"),
            "location": tr.get("data-location"),
            "link": "https://remoteok.com" + tr.get("data-href"),
        }
        if job["title"]:
            jobs.append(job)

    conn = sqlite3.connect("app/jobs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS jobs (title TEXT, company TEXT, location TEXT, link TEXT)")
    cursor.execute("DELETE FROM jobs")  # Optional: clear previous entries
    for job in jobs:
        cursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?)", tuple(job.values()))
    conn.commit()
    conn.close()
