from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    name = State()
    in_menu = State()
    adding_balance = State()
    first_wallet = State()
    wallet = State()
    getting_balance = State()






