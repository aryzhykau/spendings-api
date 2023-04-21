from aiogram.dispatcher.filters.state import State, StatesGroup


class WalletMenuState(StatesGroup):
    idle = State()
    create = State()
    remove = State()
    balance = State()
    get_all = State()