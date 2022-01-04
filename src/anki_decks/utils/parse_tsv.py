def parse_tsv(s: str):
    for line in s.strip().split('\n'):
        lst = line.split('\t')
        yield [el.strip() for el in lst]
