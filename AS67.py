import random

# Define the card names and their corresponding scoring values
cards = {
    'Card1': 5,
    'Card2': 3,
    'Card3': 7,
    'Card4': 2,
    'Card5': 6,
    'Card6': 4,
    'Card7': 9,
    'Card8': 1,
    'Card9': 8,
    'Card10': 10
}

# Function to simulate the game
def play_game():
    player1 = []
    player2 = []

    available_cards = list(cards.keys())  # List of available cards

    # Randomly assign 5 cards to each player
    for _ in range(5):
        card = random.choice(available_cards)
        player1.append(card)
        available_cards.remove(card)

        card = random.choice(available_cards)
        player2.append(card)
        available_cards.remove(card)

    print("Player 1's cards:", player1)
    print("Player 2's cards:", player2)

    player1_score = 0
    player2_score = 0

    # Compare the scoring values of the played cards
    for i in range(5):
        p1_card = player1[i]
        p2_card = player2[i]

        if cards[p1_card] > cards[p2_card]:
            player1_score += 1
        elif cards[p1_card] < cards[p2_card]:
            player2_score += 1

    print("Player 1's score:", player1_score)
    print("Player 2's score:", player2_score)

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player1_score < player2_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Play the game
play_game()
