from cardbot import card_game

cards = card_game.get_cards()
print(*cards)

def get_card_value(card):
    if card.startswith("10") or card[1] in "JQK":
        return 10
    elif card[1] == "A":
        return 12
    elif card[1] in "23456789":
        return int(card[1])
    return 0  


def chips_counter(cards):
    return [get_card_value(card) for card in cards]

print(*chips_counter(cards))