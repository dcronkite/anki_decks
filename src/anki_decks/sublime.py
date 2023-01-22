import genanki

from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.sublime_data import shortcuts
from anki_decks.utils.decks import write_deck_to_file

DECK_ID = 12077563325


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'Sublime', hotkey_first=True)
    write_deck_to_file(deck, 'sublime')


if __name__ == '__main__':
    main()
