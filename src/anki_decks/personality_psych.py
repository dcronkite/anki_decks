from pathlib import Path

import genanki

from anki_decks.utils.parse_tsv import parse_tsv_from_file
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 11783428918
DATA_PATH = Path(__file__).parent / 'data' / 'personality_psych_data.csv'

MODEL = genanki.Model(
    911783428918,
    'Personality Psychology Model',
    fields=[
        {'name': 'Model'},
        {'name': 'Target'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Model}}: {{Target}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Model}}: {{Description}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Target}}',
        },
    ]
)


def get_personality_psychology():
    deck = genanki.Deck(
        DECK_ID, 'Personality Psychology',
    )
    for model, target, description in parse_tsv_from_file(DATA_PATH, expected=3, sep='=='):
        note = genanki.Note(
            model=MODEL,
            fields=[model, target, description],
        )
        deck.add_note(note)
    genanki.Package(deck).write_to_file(f'personality_psych_{get_timestamp()}.apkg')


if __name__ == '__main__':
    get_personality_psychology()
