import genanki

from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.sublime_data import shortcuts
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 12077563325


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'Sublime', reverse=True)
    genanki.Package(deck).write_to_file(f'sublime_{get_timestamp()}.apkg')


if __name__ == '__main__':
    main()
