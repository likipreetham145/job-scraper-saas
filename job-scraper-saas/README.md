# Job Scraper Dashboard
A real-time job scraping tool with Flask dashboard and resume-based ranking.
# 💼 JobScraperSaaS — Real-Time Job Scraper with Resume Matching

A full-stack real-time job scraping platform built using Python, Flask, Selenium, and NLP.  
It scrapes job postings from top job boards, analyzes them against your resume using NLP, and serves a real-time dashboard to explore matching roles.

---

## 🔍 Features

- ✅ Real-time job scraping from RemoteOK, WeWorkRemotely, Indeed, Dice
- ✅ Resume upload with NLP-based matching
- ✅ Flask-powered dashboard
- ✅ Modular, extensible scraper system
- ✅ Scheduler to auto-refresh jobs every 30 minutes
- ✅ Docker + Render/Heroku-ready
- 🚧 Placeholder support for LinkedIn and Glassdoor (login required)

---



## 🧰 Tech Stack

- **Backend:** Flask, SQLite, Python
- **Scraping:** Selenium, BeautifulSoup
- **Matching:** Scikit-learn (TF-IDF + cosine similarity)
- **Scheduler:** Python `schedule`
- **Deployment:** Docker, Heroku, Render (optional)
- **Future Frontend:** React (WIP)

---

## 🚀 Quick Start

```bash
git clone https://github.com/likipreetham145/job-scraper-saas.git
cd job-scraper-saas
pip install -r requirements.txt
python jobscheduler.py   # Scrapes jobs every 30 mins
python app/app.py        # Starts Flask dashboard

---

## 🚀 Running the Project


🔁 Start the Job Scraper (Scheduler)

python jobscheduler.py

---
🌐 Start the Flask App

python app/app.py

Then open: http://localhost:5000

📂 Folder Structure

job-scraper-saas/
├── app/
│   ├── scraper/          # Individual scraper modules
│   ├── matcher/          # Resume NLP scoring
│   ├── templates/        # Flask HTML
│   ├── static/           # CSS and images
│   ├── routes.py         # Flask route logic
│   └── app.py            # App entry
├── data/                 # Resume input
├── jobscheduler.py       # Auto-scraping job
├── requirements.txt
├── Dockerfile
├── Procfile
├── .gitignore
└── README.md

🐳 Docker (Optional)
docker build -t job-scraper .
docker run -p 5000:5000 job-scraper

🚀 Deployment
▶️ Deploy to Heroku
Add a Procfile:
web: python app/app.py
Push to Heroku:
heroku create
git push heroku main

🌍 Deploy to Render
1. Push to GitHub
2. Create Web Service on https://render.com
3. Select repo, use:
  Start command: python app/app.py

📈 Matching Algorithm
Uses CountVectorizer + cosine_similarity from scikit-learn
Ranks all jobs against the uploaded resume
Displays top 10 matching roles with similarity %

🛣️ Roadmap
 Real-time scraping
 Resume-based job ranking
 Scheduler with schedule
 Docker support
 React frontend
 LinkedIn / Glassdoor scraping (w/ login)
 PostgreSQL + User Auth
 Email alerts for matching jobs

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Connect
Author: Likitha yellinedi


