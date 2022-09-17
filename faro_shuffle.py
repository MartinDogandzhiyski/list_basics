
deck_shuffle = input().split(" ")
number_of_shuffles = int(input())
left_half = []
right_half = []
for shuffle in range(number_of_shuffles):
    current_deck = []
    half = int(len(deck_shuffle)/2)
    left_half = deck_shuffle[0:half]
    right_half = deck_shuffle[half::]
    for card in range(len(left_half)):
        current_deck.append(left_half[card])
        current_deck.append(right_half[card])
    deck_shuffle = current_deck
print(deck_shuffle)
