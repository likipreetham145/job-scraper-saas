from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_indeed():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://www.indeed.com/jobs?q=software+engineer&l=Remote")
    time.sleep(3)

    jobs = []
    listings = driver.find_elements(By.CSS_SELECTOR, ".job_seen_beacon")
    for job_elem in listings[:10]:
        try:
            title = job_elem.find_element(By.CSS_SELECTOR, "h2.jobTitle").text
            company = job_elem.find_element(By.CSS_SELECTOR, ".companyName").text
            location = job_elem.find_element(By.CSS_SELECTOR, ".companyLocation").text
            link = job_elem.find_element(By.TAG_NAME, "a").get_attribute("href")

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
