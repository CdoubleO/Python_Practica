from enum import Enum, auto

class Suite(Enum):
    DIAMOND = auto()
    SPADE = auto()
    HEART = auto()
    CLUB = auto()


class Value(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Card:
    def __init__(
        self,
        value,
        suite
                ):

        self.value = value
        self.suite = suite

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value: Value):
        if value not in Value:
            raise Exception
        self._value = value

    @property
    def suite(self):
           return self._suite
    @suite.setter
    def suite(self, suite: Suite):
        if suite not in Suite:
            raise Exception
        self._suite = suite
        
    def __repr__(self):
        return f'<Card {self.value} {self.suite}>'

  
class Deck:
    def __init__(self):
        self.cards = [Card(v,s) for v in Value for s in Suite]


    def __repr__(self):
        return ''.join([f'\n{c}' for c in self.cards])




























    
    
