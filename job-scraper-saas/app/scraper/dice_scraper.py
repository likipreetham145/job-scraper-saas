from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_dice():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://www.dice.com/jobs?q=software+engineer&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20")
    time.sleep(5)

    jobs = []
    listings = driver.find_elements(By.CSS_SELECTOR, ".card")
    for job_elem in listings[:10]:
        try:
            title = job_elem.find_element(By.CSS_SELECTOR, ".card-title-link").text
            company = job_elem.find_element(By.CSS_SELECTOR, ".card-company").text
            location = job_elem.find_element(By.CSS_SELECTOR, ".card-location").text
            link = job_elem.find_element(By.CSS_SELECTOR, ".card-title-link").get_attribute("href")

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link
            })
        except:
            continue

    driver.quit()
    return jobs
