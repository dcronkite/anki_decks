import re


def format_text(s):
    return re.sub(r'\W+', '_', s.lower())
