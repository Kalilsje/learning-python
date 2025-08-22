import random
class Card:
    def __init__(self, card_suit, card_rank) -> None:
        self.suit = card_suit
        self.rank = card_rank
    
    def show(self):
        return f"{self.suit} - {self.rank}"
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def rank(self):
        return self._rank
    
    @suit.setter
    def suit(self, value):
        if value in ["ouros", "copas", "espadas", "paus"]:
            self._suit = value
        else:
            raise ValueError("Naipe invalido")

    @rank.setter
    def rank(self, value):
        if value >= 1 and value >= 13:
            self._rank = value
        else:
            raise ValueError("Valor Invalido")

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
    
    def generate_deck(self):
        list_of_cards = []
        for suit in ["ouros", "espadas", "paus", "copas"]:
            for rank in range(0, 13):
                list_of_cards.append(Card(suit, rank+1))
                return list_of_cards

    def create_deck(self):
        self.cards = self.generate_deck()

    def show(self):
        for card in self.cards:
            print(card.show())

    def append_card(self, card: Card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()
    
    def shuffle(self):
        for card_i in range(len(self.cards)-1, 0, -1):
            card_j = random.randint(0, card_i)
            self.cards[card_i], self.cards[card_j] = self.cards[card_j], self.cards[card_i]


deck = Deck()
deck.shuffle()
deck.show()