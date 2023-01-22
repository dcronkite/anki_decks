import genanki

from anki_decks.utils.decks import write_deck_to_file
from anki_decks.utils.parse_table import parse_wikipedia_table

DECK_ID = 11683463763


def get_dynasties():
    url = r'https://en.wikipedia.org/wiki/Dynasties_of_ancient_Egypt'
    headers, data = list(parse_wikipedia_table(url))[0]
    model = genanki.Model(
        91353952151,
        'Dynasty Model',
        fields=[
            {'name': 'Dynasty'},
            {'name': 'Years'},
            {'name': 'Period'},
            {'name': 'NumberYears'},
            {'name': 'Capital'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Dynasty}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Period}}\n{{Years}} ({{NumberYears}})\n{{Capital}}',
            },
            {
                'name': 'Card 2',
                'qfmt': '{{Years}} (Dynasty)',
                'afmt': '{{FrontSide}}<hr id="answer">{{Dynasty}} ({{Period}})',
            },
        ]
    )
    for row in data:
        if len(row) < 9:
            continue
        dynasty_name = row[0]
        capital = row[1]
        start_year = row[2]
        end_year = row[3]
        num_years = row[4]
        period = row[-1]
        if start_year.lower() == 'unknown':
            continue
        yield genanki.Note(
            model=model,
            fields=[dynasty_name, f'{start_year} - {end_year}', period, num_years, capital]
        )


def get_rulers_after_18th_dynasty():
    url = r'https://en.wikipedia.org/wiki/List_of_pharaohs'
    model = genanki.Model(
        915328397981,
        'Ruler Model',
        fields=[
            {'name': 'PersonalName'},
            {'name': 'ThroneName'},
            {'name': 'Comments'},
            {'name': 'Dates'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{PersonalName}} ({{ThroneName}})',
                'afmt': '{{FrontSide}}<hr id="answer">{{Dates}}\n{{Comments}}',
            },
            {
                'name': 'Card 2',
                'qfmt': '{{Dates}} (Ruler)',
                'afmt': '{{FrontSide}}<hr id="answer">{{PersonalName}}\n{{ThroneName}}\n{{Comments}}',
            },
        ]
    )
    for headers, data in parse_wikipedia_table(url, start_at={'id': 'New_Kingdom'}):
        for row in data:
            if len(row) < 3:
                continue
            if 'Name' in headers:
                throne_name = row[1]
                personal_name = row[1]
                comments = row[2]
                dates = row[3].split(';')[0]
            else:
                throne_name = row[1]
                personal_name = row[2]
                comments = row[3]
                dates = row[4].split(';')[0]
            yield genanki.Note(
                model=model,
                fields=[throne_name, personal_name, comments, dates]
            )


def main():
    deck = genanki.Deck(
        DECK_ID,
        'Ancient Egypt',
    )
    for note in get_dynasties():
        deck.add_note(note)
    for note in get_rulers_after_18th_dynasty():
        deck.add_note(note)
    write_deck_to_file(deck, 'ancient_egypt')


if __name__ == '__main__':
    main()
