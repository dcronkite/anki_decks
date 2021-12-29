import datetime

import genanki

from anki_decks.utils.parse_table import parse_wikipedia_table

MODEL_ID = 91353952151
DECK_ID = 11683463763


def main():
    url = r'https://en.wikipedia.org/wiki/Dynasties_of_ancient_Egypt'
    headers, data = list(parse_wikipedia_table(url))[0]
    model = genanki.Model(
        MODEL_ID,
        'Simple Model',
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
    deck = genanki.Deck(
        DECK_ID,
        'Ancient Egypt',
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
        deck.add_note(
            genanki.Note(
                model=model,
                fields=[dynasty_name, f'{start_year} - {end_year}', period, num_years, capital]
            )
        )
    genanki.Package(deck).write_to_file(f'ancient_egypt_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.apkg')


if __name__ == '__main__':
    main()
