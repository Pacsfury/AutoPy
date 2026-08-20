import subprocess
import helpers as h

def run(cmd):
    result = subprocess.run(
        h._safe_split(cmd), 
        capture_output=True, 
        text=True, 
        check=True,
        shell=True
    )
    return result.stdout.strip()
