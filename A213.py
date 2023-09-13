import random

class Card:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self):
        return self.cards.pop(0)

class CardGame:
    def __init__(self, players):
        self.players = players
        self.cards = [
            Card('Card1', 5),
            Card('Card2', 3),
            Card('Card3', 7),
            Card('Card4', 2),
            Card('Card5', 6),
            Card('Card6', 4),
            Card('Card7', 9),
            Card('Card8', 1),
            Card('Card9', 8),
            Card('Card10', 10)
        ]

    def play(self):
        random.shuffle(self.cards)

        for player in self.players:
            for _ in range(5):
                card = self.cards.pop()
                player.add_card(card)

        for round_num in range(5):
            print(f"Round {round_num + 1}:")

            played_cards = []

            for player in self.players:
                played_card = player.play_card()
                played_cards.append(played_card)

                print(f"{player.name} played {played_card.name}")

            winning_card = max(played_cards, key=lambda card: card.score)
            winner = [player for player, card in zip(self.players, played_cards) if card == winning_card]
            winner_names = [player.name for player in winner]

            print(f"Winner(s) of the round: {', '.join(winner_names)}\n")

if __name__ == '__main__':
    player1 = Player('Player 1')
    player2 = Player('Player 2')

    game = CardGame([player1, player2])
    game.play()
