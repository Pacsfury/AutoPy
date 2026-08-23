# AutoPy

Automation tool for compilation and execution
_vAlpha 0.0.1_

---

## What is it

With AutoPy, you can automize jobs through a JSON. These jobs are executing some commands.

## How to use it

Example for executing a Python file:

`AUTOPY.json`
```json
{
    "jobs": [
        {
            "compiler": "python",
            "id": "test1", // Optional: use the id as argument to call only this
            "flags": [
                "-u"
            ],
            "input": "TEST1.py",
            "output": "",
            "outputSymbol": ""
        },
        {
            "compiler": "python",
            "id": "test2",
            "flags": [
                "-u"
            ],
            "input": "TEST2.py",
            "output": "",
            "outputSymbol": ""
        },
        {
            "compiler": "gcc",
            "id": "gcc",
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
