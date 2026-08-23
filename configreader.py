import json
import main
import sys

def process_job(job):
    global COMPILER, FLAGS, OUTPUT, OUTPUTCMD, INPUT
    COMPILER = job.get("compiler")
    FLAGS = job.get("flags")
    OUTPUT = job.get("output")
    OUTPUTCMD = job.get("outputSymbol", "") + OUTPUT
    INPUT = job.get("input")

    main.runConfig()
    

with open('AUTOPY.json', 'r', encoding='utf-8') as config:
    data = json.load(config)

jobs = data.get("jobs", [])
if len(sys.argv) == 1:
    for job in jobs:
        process_job(job)
else:
    for job in jobs:
        if job.get("id") == sys.argv[1]:
            process_job(job)
