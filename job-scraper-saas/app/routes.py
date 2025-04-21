from flask import Flask, render_template, request
from .scraper.remoteok_scraper import scrape_and_store_jobs
from .matcher.resume_matcher import match_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    if request.method == "POST":
        resume = request.files["resume"]
        if resume:
            text = resume.read().decode("utf-8")
            jobs = match_resume(text)
    return render_template("index.html", jobs=jobs)
