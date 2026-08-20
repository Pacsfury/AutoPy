# AutoPy

Automation tool for compilation and execution
_vAlpha 0.0.1_

---

## What is it

With AutoPy, you can automize jobs through a JSON. These jobs are executing some commands.

## How to use it

Example for executing a Python file:
```json
{
    "jobs": [
        /* 
        Every job includes some basic fields:
        */
        {
            "compiler": "python",
            "flags": [
                "-u"
            ],
            "input": "TEST1.py",
            "output": "",
            "outputSymbol": ""
        },
        {
            "compiler": "python",
            "flags": [
                "-u"
            ],
            "input": "TEST2.py",
            "output": "",
            "outputSymbol": ""
        },
        {
            "compiler": "gcc",
            "flags": [
                "-Wall"
            ],
            "input": "src/*.c",
            "output": "result",
            "outputSymbol": "-o "
        }
    ]
}
```

> AutoPy is in process: major features and improvements are coming soon