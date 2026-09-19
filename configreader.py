import json
import sys
from pathlib import Path


def load_jobs(config_path="AUTOPY.json"):
    with open(Path(config_path), "r", encoding="utf-8") as config:
        data = json.load(config)
    return data.get("jobs", [])


def process_job(job):
    global COMPILER, FLAGS, OUTPUT, OUTPUTCMD, INPUT
    COMPILER = job.get("compiler")
    FLAGS = job.get("flags", [])
    OUTPUT = job.get("output")
    OUTPUTCMD = job.get("outputSymbol", "") + str(OUTPUT or "")
    INPUT = job.get("input")
    return job


def load_selected_job(config_path="AUTOPY.json", job_id=None):
    jobs = load_jobs(config_path)
    if not jobs:
        raise ValueError("No jobs found in AUTOPY.json")

    selected = job_id
    if selected is None and len(sys.argv) > 1 and sys.argv[1] != "--version":
        selected = sys.argv[1]

    if selected is None:
        for job in jobs:
            process_job(job)
        return jobs

    for job in jobs:
        if job.get("id") == selected:
            return process_job(job)

    raise ValueError(f"Job '{selected}' was not found in AUTOPY.json")
