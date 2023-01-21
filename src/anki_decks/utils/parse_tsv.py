def parse_tsv(s: str, *, expected=None, linesep='\n', sep='\t'):
    for line in s.strip().split(linesep):
        lst = line.split(sep)
        if expected and len(lst) != expected:
            raise ValueError(f'Only found {len(lst)} elements in line: {line}')
        yield [el.strip() for el in lst]


def parse_tsv_from_file(path, *, expected=None, linesep='\n', sep='\t', encoding='utf8'):
    with open(path, encoding=encoding) as fh:
        yield from parse_tsv(fh.read(), expected=expected, linesep=linesep, sep=sep)
