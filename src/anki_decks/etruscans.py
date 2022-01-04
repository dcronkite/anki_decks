import datetime

import genanki

DECK_ID = 12117317529


def get_chronology():
    model = genanki.Model(
        91083544126,
        'Chronology Model',
        fields=[
            {'name': 'Period'},
            {'name': 'Years'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Period}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Years}}',
            },
            {
                'name': 'Card 2',
                'qfmt': '{{Years}} (Period)',
                'afmt': '{{FrontSide}}<hr id="answer">{{Period}}',
            },
        ]
    )
    data = [
        ('Villanovan Period', '900-720 BC'),
        ('Orientalizing Period', '720-580 BC'),
        ('Archaic Period', '580-480 BC'),
        ('Classical Period', '480-320 BC'),
        ('Hellenistic Period', '320-27 BC'),
        ('Villanovan I', '900–800 BC'),
        ('Villanovan II', '800–720 BC'),
        ('Villanovan III (Bologna area)', '720–680 BC'),
        ('Villanovan IV (Bologna area)', '680–540 BC'),
        ('Early Orientalizing', '720–680 BC'),
        ('Middle Orientalizing', '680–625 BC'),
        ('Late Orientalizing', '625–580 BC'),
    ]
    for period, years in data:
        yield genanki.Note(
            model=model,
            fields=[period, years]
        )


def main():
    deck = genanki.Deck(
        DECK_ID,
        'Etruscans',
    )
    for note in get_chronology():
        deck.add_note(note)
    genanki.Package(deck).write_to_file(f'etruscans_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.apkg')


if __name__ == '__main__':
    main()
