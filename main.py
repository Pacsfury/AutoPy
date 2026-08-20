import subprocess
import configreader as cr

cmd = [cr.COMPILER.strip()] + cr.FLAGS + [cr.INPUT.strip(), cr.OUTPUTCMP.strip()]

result = subprocess.run(
    cmd, 
    capture_output=True, 
    text=True, 
    check=True,
    shell=True
)

print(result.stdout)
