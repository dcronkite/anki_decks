import genanki

from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.pycharm_mac_data import shortcuts
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 11707139697


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'Pycharm Mac')
    genanki.Package(deck).write_to_file(f'pycharm_mac_{get_timestamp()}.apkg')


if __name__ == '__main__':
    main()
