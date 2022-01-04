"""
Build hotkeys: assumes 2 columns separated by tabs.
"""
import genanki

from anki_decks.utils.parse_tsv import parse_tsv

MODEL = genanki.Model(
    91912714754,
    'Hotkey Model',
    fields=[
        {'name': 'Hotkey'},
        {'name': 'Action'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Hotkey}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Action}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Action}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Hotkey}}',
        },
    ]
)


def build_hotkey_deck(tsv_data: str, deck_id: int, deck_name: str, hotkey_first=False):
    """

    :param tsv_data:
    :param deck_id:
    :param deck_name:
    :param hotkey_first: if hotkey appears before action, set this to True
    :return:
    """
    deck = genanki.Deck(
        deck_id, deck_name
    )

    for action, hotkey in parse_tsv(tsv_data, expected=2):
        if hotkey_first:
            action, hotkey = hotkey, action
        note = genanki.Note(
            model=MODEL,
            fields=[hotkey, action]
        )
        deck.add_note(note)
    return deck
