import genanki

from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.pycharm_mac_data import shortcuts
from anki_decks.utils.decks import write_deck_to_file
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 11707139697


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'Pycharm Mac')
    write_deck_to_file(deck, 'pycharm_mac')


if __name__ == '__main__':
    main()
