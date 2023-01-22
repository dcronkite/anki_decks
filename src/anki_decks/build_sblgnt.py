from pathlib import Path

import genanki

from anki_decks.utils.clean import format_text
from anki_decks.utils.decks import get_subcategory_deck, write_deck_to_file
from anki_decks.utils.parse_tsv import parse_tsv_from_file
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 12039345762
DATA_PATH = Path(__file__).parent / 'data' / 'sblgnt.csv'

MODEL = genanki.Model(
    92039345762,
    'SBL GNT Model',
    fields=[
        {'name': 'Book'},
        {'name': 'Verse'},
        {'name': 'Line'},
        {'name': 'PrevLine'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Book}} {{Verse}}<br>{{PrevLine}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Line}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{PrevLine}}<br>{{Line}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Author}}: {{Title}}',
        },
    ]
)


def _get_sblgnt_deck(label):
    return get_subcategory_deck(DECK_ID, 'SBLGNT', label)


def build_sblgnt_decks():
    prev_line = ''
    prev_book = None
    deck = None
    book = None
    for book, verse, line in parse_tsv_from_file(DATA_PATH, expected=3, sep='=='):
        if book != prev_book:
            if deck is not None:
                write_deck_to_file(deck, format_text(prev_book))
            prev_book = book
            deck = _get_sblgnt_deck(book)
        note = genanki.Note(
            model=MODEL,
            fields=[book, verse, line, prev_line],
        )
        deck.add_note(note)
        prev_line = line
    if book is not None:
        write_deck_to_file(deck, format_text(book))


if __name__ == '__main__':
    build_sblgnt_decks()
