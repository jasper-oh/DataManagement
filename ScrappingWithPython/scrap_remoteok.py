import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


def extract_job(job):
    name = job.find("h2", {"itemprop": "title"}).get_text(strip=True)
    company = job['data-company']
    job_id = job['data-id']
    url = f'https://remoteok.io/remote-jobs/{job_id}'
    website = "Remote OK"
    return {
        "name": name,
        "company": company,
        "url": url,
        'website': website
    }


def extract_job_list(URL):
    jobs = []
    result = requests.get(URL, headers=headers)
    print(f"Scrapping Jobs from: {URL}")
    soup = BeautifulSoup(result.text, 'html.parser')
    job_collect = soup.find_all("tr", {"class": "job"})
    for job in job_collect:
        job_info = extract_job(job)
        jobs.append(job_info)
    return jobs


def get_jobs(lang_name):
    URL = f"https://remoteok.io/remote-dev+{lang_name}-jobs"
    jobs = extract_job_list(URL)
    return jobs
