from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import random

TOKEN = '8495932018:AAHW2TycvUj0m42rcSj5o5SyPo4r6gTNXI0'
bot = Bot(TOKEN)
dp = Dispatcher()

class CardGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.enemy_hand = []
        self.player_score = 0
        self.enemy_score = 0

    def create_deck(self):
        suits = ["♥", "♦", "♣", "♠"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [f"{suit}{value}" for suit in suits for value in values]
        random.shuffle(deck)
        return deck

    def get_cards(self):
        empty_slots = 6 - len(self.player_hand)
        for i in range(empty_slots):
            card = self.deck.pop()
            self.player_hand.append(card)
        return self.player_hand
    
    def set_cards(self):
        self.player_hand = []
        for i in range(6):
            card = self.deck.pop()
            self.player_hand.append(card)
        return self.player_hand

    def look_cards(self):
        return self.deck
        
card_game = CardGame()
deck = card_game.create_deck()

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

@dp.message(Command("start"))
async def bot_cards(message: Message):
        card_game.deck = card_game.create_deck()
        cards = card_game.get_cards()
        cards = "  ".join(cards)
        await message.answer("У вас есть 6 карт, Вы моженте перевыбрать карту. Сыграйте лучшую комбинацию")
        await message.answer(cards)
        
@dp.message(Command("set"))
async def bot_set_cards(message: Message):
        cards = card_game.set_cards()
        cards = "  ".join(cards)
        await message.answer("Вы меняете карты. Выши новые карты")
        await message.answer(cards)
        
@dp.message(Command("look"))
async def look(message: Message):
    look_cards = card_game.look_cards()
    look_card = "  ".join(look_cards)
    await message.answer(look_card)
    # send numeric values as a string (aiogram expects text:str)
    hand_values = chips_counter(card_game.player_hand)
    await message.answer("  ".join(map(str, hand_values)))
        
if __name__ == "__main__":
    dp.run_polling(bot)
    