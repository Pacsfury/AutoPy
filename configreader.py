import json
import sys
from pathlib import Path

COMPILER = ""
FLAGS = []
OUTPUT = ""
OUTPUTCMD = ""
INPUT = ""
COMMAND_ARGS = []


def load_jobs(config_path="AUTOPY.json"):
    with open(Path(config_path), "r", encoding="utf-8") as config:
        data = json.load(config)
    return data.get("jobs", [])


def process_job(job):
    global COMPILER, FLAGS, OUTPUT, OUTPUTCMD, INPUT, COMMAND_ARGS
    
    COMPILER = job.get("compiler", "")
    FLAGS = job.get("flags", [])
    OUTPUT = job.get("output", "")
    INPUT = job.get("input", "")
    
    # Manejo seguro del símbolo de output
    symbol = job.get("outputSymbol", "")
    if symbol and OUTPUT:
        OUTPUTCMD = f"{symbol}{OUTPUT}"
    else:
        OUTPUTCMD = str(OUTPUT)

    componentes = [COMPILER] + FLAGS + [INPUT]
    if symbol:
        componentes.append(symbol)
    if OUTPUT:
        componentes.append(OUTPUT)

    COMMAND_ARGS = [str(arg) for arg in componentes if str(arg).strip()]
    
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
