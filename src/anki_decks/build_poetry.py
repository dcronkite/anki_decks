from pathlib import Path

import genanki

from anki_decks.utils.clean import format_text
from anki_decks.utils.decks import get_deck
from anki_decks.utils.parse_tsv import parse_tsv_from_file
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 11399878920
DATA_PATH = Path(__file__).parent / 'data' / 'poetry.csv'

MODEL = genanki.Model(
    91399878920,
    'Poetry Model',
    fields=[
        {'name': 'Author'},
        {'name': 'Title'},
        {'name': 'Line'},
        {'name': 'PrevLine'},
        {'name': 'PrevPrevLine'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Author}}: {{Title}}<br>{{PrevPrevLine}}<br>{{PrevLine}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Line}}',
        },
        {
            'name': 'Card 2',
            'qfmt': 'Author/Title<br>{{Line}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Author}}: {{Title}}',
        },
    ]
)


def _get_poetry_deck(label):
    return get_deck(DECK_ID, 'Poetry', label)


def build_poetry_decks():
    prev_prev_line = ''
    prev_line = ''
    prev_label = None
    deck = None
    label = None
    for author, title, line in parse_tsv_from_file(DATA_PATH, expected=3, sep='=='):
        label = format_text(f'{author}_{title}')
        if label != prev_label:
            if deck is not None:
                genanki.Package(deck).write_to_file(f'poetry_{prev_label}_{get_timestamp()}.apkg')
            prev_label = label
            deck = _get_poetry_deck(label)
        note = genanki.Note(
            model=MODEL,
            fields=[author, title, line, prev_line, prev_prev_line],
        )
        deck.add_note(note)
    if label is not None:
        genanki.Package(deck).write_to_file(f'poetry_{label}_{get_timestamp()}.apkg')


if __name__ == '__main__':
    build_poetry_decks()
