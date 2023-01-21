import re


def format_text(s, lower=True):
    return re.sub(r'\W+', '_', s.lower() if lower else s)
