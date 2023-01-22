from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.vscode_windows_data import shortcuts
from anki_decks.utils.decks import write_deck_to_file

DECK_ID = 11188224927


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'VS Code Windows', hotkey_first=True)
    write_deck_to_file(deck, 'vscode_windows')


if __name__ == '__main__':
    main()
