import platform
import subprocess
import sys

import configreader as cr


def runConfig():
    cmd = [str(cr.COMPILER).strip()]
    if cr.FLAGS:
        cmd.extend(cr.FLAGS)
    cmd.extend([str(cr.INPUT).strip(), str(cr.OUTPUTCMD).strip()])

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        shell=False,
    )

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print("""
     _      _    _  _______   ____   _____ __     __
    / \\    | |  | ||__   __| / __ \\ |  __ \\\\ \\   / /
   / _ \\   | |  | |   | |   | |  | || |__) |\\ \\_/ / 
  / ___ \\  | |  | |   | |   | |  | ||  ___/  \\   /  
 /_/   \\_\\  \\____/    |_|    \\____/ |_|       |_|                                                    
""")
        print(f"\nAutoPy version Alpha 0.0.1\n@ {platform.system()}, {platform.processor()}")
        raise SystemExit(0)

    selected = cr.load_selected_job()
    if isinstance(selected, list):
        for job in selected:
            cr.process_job(job)
            runConfig()
    else:
        runConfig()