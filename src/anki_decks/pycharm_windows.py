from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.pycharm_windows_data import shortcuts
from anki_decks.utils.decks import write_deck_to_file

DECK_ID = 11653767316


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'Pycharm Windows')
    write_deck_to_file(deck, 'pycharm_windows')


if __name__ == '__main__':
    main()
