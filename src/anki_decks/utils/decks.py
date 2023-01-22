from pathlib import Path

import genanki

from anki_decks.utils.timestamp import get_timestamp


def get_subcategory_deck(deck_id, category, label):
    """Create deck subcategory of `category` called `label`; creates unique deck id."""
    return genanki.Deck(
        deck_id + abs(hash(label) % 1000000), f'{category}::{label}',
    )


def build_filename(name, include_timestamp=False):
    """Builds filename with or without timestamp; includes appropriate extensions."""
    if include_timestamp:
        return f'{name}_{get_timestamp()}.apkg'
    else:
        return f'{name}.apkg'


def write_deck_to_file(deck, name, *, outdir=Path('.'), include_timestamp=False):
    """Write deck to file, including generating filename."""
    genanki.Package(deck).write_to_file(outdir / build_filename(name, include_timestamp=include_timestamp))
