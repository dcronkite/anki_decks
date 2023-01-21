import genanki


def get_deck(deck_id, category, label):
    return genanki.Deck(
        deck_id + abs(hash(label) % 1000000), f'{category}::{label}',
    )
