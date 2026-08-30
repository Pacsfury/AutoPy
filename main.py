import subprocess
import configreader as cr
import sys
import platform

if sys.argv[1] == "--version" and __name__ == "__main__":
    print("""
     _      _    _  _______   ____   _____ __     __
    / \\    | |  | ||__   __| / __ \\ |  __ \\\\ \\   / /
   / _ \\   | |  | |   | |   | |  | || |__) |\\ \\_/ / 
  / ___ \\  | |  | |   | |   | |  | ||  ___/  \\   /  
 /_/   \\_\\  \\____/    |_|    \\____/ |_|       |_|                                                    
""")
    print(f"\nAutoPy version Alpha 0.0.1\n@ {platform.system()}, {platform.processor()}")


def runConfig():
    cmd = [cr.COMPILER.strip()] + cr.FLAGS + [cr.INPUT.strip(), cr.OUTPUTCMD.strip()]

    result = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True, 
        shell=True
    )

    print(result.stdout)
