import csv


def save_to_file(jobs):
    print("got jobs")
    job_file = open("jobs.csv", mode="w")
    writer = csv.writer(job_file)
    writer.writerow(["Title", "Company", "Apply link", "Platform"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
