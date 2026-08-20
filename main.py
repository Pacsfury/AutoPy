import subprocess
import configreader as cr

def runConfig():
    cmd = [cr.COMPILER.strip()] + cr.FLAGS + [cr.INPUT.strip(), cr.OUTPUTCMD.strip()]

    result = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True, 
        check=True,
        shell=True
    )

    print(result.stdout)
