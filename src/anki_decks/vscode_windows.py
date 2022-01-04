import genanki

from anki_decks.hotkeys.build_hotkey_deck import build_hotkey_deck
from anki_decks.hotkeys.vscode_windows_data import shortcuts
from anki_decks.utils.timestamp import get_timestamp

DECK_ID = 11188224927


def main():
    deck = build_hotkey_deck(shortcuts, DECK_ID, 'VS Code Windows', hotkey_first=True)
    genanki.Package(deck).write_to_file(f'vscode_windows_{get_timestamp()}.apkg')


if __name__ == '__main__':
    main()
