import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isValidNumber(string: str):
    try:
        float(string)
        return True
    except ValueError:
        return False


def convertToNumber(string: str):
    newString = float(string) if '.' in string else int(string)
    return newString
