import json

def parse(filename):
    try:
        strings = open(filename).readlines()
        string = ""
        for s in strings:
            string += s
        return json.loads(string)
    except IOError:
        return None
