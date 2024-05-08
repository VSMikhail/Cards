class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.symbols = (
            ('２ ', '３ ', '４ ', '５ ', '６ ', '７ ', '８ ', '９ ', '１０', '👨', '👸🏻', '🤴🏻', 'A '),
            ('❤', '♠', '♣', '♦'),
            ('|', '―')
        )

    def __str__(self):
        return f'|{self.symbols[0][self.rank - 2]} ― {self.symbols[1][self.suit - 1]}|'

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.rank < other.rank
        else:
            return None

    def __le__(self, other):
        if self.suit == other.suit:
            return self.rank <= other.rank
        else:
            return None

    def __gt__(self, other):
        if self.suit == other.suit:
            return self.rank > other.rank
        else:
            return None

    def __ge__(self, other):
        if self.suit == other.suit:
            return self.rank >= other.rank
        else:
            return None
    def __eq__(self, other):
        return self.rank == other.rank