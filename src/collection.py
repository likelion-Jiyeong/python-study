import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards) + 10
    
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck))

class TestClass:
    def __init__(self) -> None:
        pass
        
    # def __repr__(self):
    #     return 'This is an example!!'

test = TestClass()
print(test)