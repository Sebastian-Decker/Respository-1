class Card:
    def __init__(self, soft_rank, hard_rank, suit):
        self.__soft_rank = soft_rank
        self.__hard_rank = hard_rank
        self.__suit = suit

class AceCard(Card):
    def __init__(self, suit):
        Card.__init__(self, 11, 1, suit)
        self.__face = 'A'

class FaceCard(Card):
    def __init__(self, suit, face):
        Card.__init__(self, 10, 10, suit)
        self.face = face

    def get_suit(self):
        return self.__suit

    def get_suit(self):
        return self.__number

    def __str__(self):
        return f"Suit: {self.__suit}\nNumber: {self.__number}"
