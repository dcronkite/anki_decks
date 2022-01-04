def parse_tsv(s: str, *, expected=None, linesep='\n', sep='\t'):
    for line in s.strip().split(linesep):
        lst = line.split(sep)
        if expected and len(lst) != expected:
            raise ValueError(f'Only found {len(lst)} elements in line: {line}')
        yield [el.strip() for el in lst]
