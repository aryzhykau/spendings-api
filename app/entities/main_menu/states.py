from aiogram.dispatcher.filters.state import State, StatesGroup

class MainMenuState(StatesGroup):
    welcome = State()
    idle = State()
    first_wallet = State()
