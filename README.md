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
    "compiler": "python",    // What compiler?
    "flags": [               // What flags?
        "-u"
    ],
    "input": "TEST.py",      // What file(s)?
    "output": "",            // How will be the output named?
    "outputSymbol": ""       // How does your compiler mark the output? (-o, /Fe:, etc)
}
```

> AutoPy is in process: major features and improvements are coming soon