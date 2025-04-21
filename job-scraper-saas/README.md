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
