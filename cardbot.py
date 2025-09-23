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
        for i in range(6):
            card = self.deck.pop()
            self.player_hand.append(card)
        return self.player_hand

card_game = CardGame()
deck = card_game.create_deck()

@dp.message(Command("start"))
async def start(message: Message):
        cards = card_game.get_cards()
        cards = "  ".join(cards)
        await message.answer("У вас есть 6 карт, Вы моженте перевыбрать карту. Сыграйте лучшую комбинацию")
        await message.answer(cards)
        
if __name__ == "__main__":
    dp.run_polling(bot)