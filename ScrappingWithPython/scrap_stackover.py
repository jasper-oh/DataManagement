import requests
from bs4 import BeautifulSoup


def extract_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    try:
        pages = soup.find_all("a", {"class": "s-pagination--item"})
        last_page = pages[-2].get_text()
    except:
        last_page = 1
    return int(last_page)


def extract_job(job):
    name = job.find("a", {"class": "s-link"}).get_text(strip=True)
    company = job.find("h3", {"class": "mb4"}).find(
        "span").get_text(strip=True)
    job_id = job['data-result-id']
    url = f"https://stackoverflow.com/jobs/{job_id}"
    website = "Stack Overflow"
    return {
        "name": name,
        "company": company,
        "url": url,
        'website': website
    }


def extract_job_list(last_page, URL):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}{page+1}")
        print(f"Scrapping Stack Overflow page {page+1}: {result.status_code}")
        soup = BeautifulSoup(result.text, 'html.parser')
        job_list = soup.find_all("div", {"class": "-job"})
        for job in job_list:
            job_info = extract_job(job)
            jobs.append(job_info)
    return jobs


def get_jobs(lang_name):
    URL = f"https://stackoverflow.com/jobs?r=true&q={lang_name}"
    last_page = extract_last_page(URL)
    jobs = extract_job_list(last_page, URL)
    return jobs
