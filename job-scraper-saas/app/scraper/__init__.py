from .remoteok_scraper import scrape_remoteok
from .weworkremotely_scraper import scrape_weworkremotely
from .indeed_scraper import scrape_indeed
from .dice_scraper import scrape_dice
from .linkedin_scraper import scrape_linkedin
from .glassdoor_scraper import scrape_glassdoor
import sqlite3

def scrape_and_store_all_jobs():
    all_jobs = []
    for scraper_func in [
        scrape_remoteok,
        scrape_weworkremotely,
        scrape_indeed,
        scrape_dice,
        scrape_linkedin,
        scrape_glassdoor
    ]:
        try:
            jobs = scraper_func()
            all_jobs.extend(jobs)
        except Exception as e:
            print(f"[ERROR] {scraper_func.__name__}: {e}")

    conn = sqlite3.connect("app/jobs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS jobs (title TEXT, company TEXT, location TEXT, link TEXT)")
    cursor.execute("DELETE FROM jobs")
    for job in all_jobs:
        cursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?)", tuple(job.values()))
    conn.commit()
    conn.close()
