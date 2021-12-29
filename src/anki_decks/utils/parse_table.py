import requests
from bs4 import BeautifulSoup


def find_all(soup, element, start_at=None, **kwargs):
    if start_at:
        soup = soup.find(**start_at)
        yield from soup.find_all_next(element, **kwargs)
    else:
        yield from soup.find_all(element, **kwargs)


def parse_wikipedia_table(url, start_at=None):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    for table in find_all(soup, 'table', start_at=start_at, class_='wikitable'):
        headers = []
        data = []
        append_to_all_rows = []
        for row_num, row in enumerate(table.tbody.find_all('tr')):
            i = 0
            if columns := row.find_all('th'):
                if len(columns) == 1:
                    append_to_all_rows = [columns[0].text.strip()]
                    continue
                for column in columns:
                    if len(headers) <= i:  # header already exists
                        if 'rowspan' in column.attrs:
                            for j in range(int(column.attrs['rowspan'])):
                                headers.append(column.text.strip())
                                i += 1
                        else:
                            headers.append(column.text.strip())
                            i += 1
                    else:
                        if 'rowspan' in column.attrs:
                            for j in range(int(column.attrs['rowspan'])):
                                headers[i] += f' - {column.text.strip()}'
                                i += 1
                        else:
                            headers[i] += f' - {column.text.strip()}'
                            i += 1
            elif columns := row.find_all('td'):
                row_data = []
                for column in columns:
                    if 'rowspan' in column.attrs:
                        for j in range(column.attrs['rowspan']):
                            row_data.append(column.text.strip())
                            i += 1
                    else:
                        row_data.append(column.text.strip())
                        i += 1
                row_data += append_to_all_rows
                data.append(row_data)
            else:
                pass
        yield headers, data
