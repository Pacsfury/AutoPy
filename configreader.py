import json

with open('AUTOPY.json', 'r', encoding='utf-8') as config:
    data = json.load(config)

def getPropierty(name):
    return data[name]

COMPILER = getPropierty("compiler")
FLAGS = getPropierty("flags")
OUTPUT = getPropierty("output")
OUTPUTCMP = getPropierty("outputSymbol") + OUTPUT
INPUT = getPropierty("input")
