import schedule
import time
from app.scraper.remoteok_scraper import scrape_and_store_jobs

schedule.every(30).minutes.do(scrape_and_store_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)
