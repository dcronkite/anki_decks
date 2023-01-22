import re


def format_text(s, lower=True):
    """Replace non-letter characters with underscore. Option to lowercase."""
    return re.sub(r'\W+', '_', s.lower() if lower else s)
