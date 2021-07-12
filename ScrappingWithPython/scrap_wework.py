import requests
from bs4 import BeautifulSoup


def extract_job(job):
    name = job.find("span", {"class": "title"}).get_text()
    company = job.find("span", {"class": "company"}).get_text()
    job_route = job['href']
    url = f'https://weworkremotely.com{job_route}'
    website = "We Work"
    return {
        "name": name,
        "company": company,
        "url": url,
        'website': website
    }


def extract_job_list(URL):
    jobs = []
    result = requests.get(URL)
    print(f"Scrapping jobs from: {URL}")
    soup = BeautifulSoup(result.text, 'html.parser')
    job_section = soup.find_all("section", {"class": "jobs"})
    for job_list in job_section:
        job_list = job_list.find_all("li")
        for job in job_list[:-1]:
            job = job.find("a", recursive=False)
            job_info = extract_job(job)
            jobs.append(job_info)
    return jobs


def get_jobs(lang_name):
    URL = f"https://weworkremotely.com/remote-jobs/search?term={lang_name}"
    jobs = extract_job_list(URL)
    return jobs
