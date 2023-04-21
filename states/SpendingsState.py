from aiogram.dispatcher.filters.state import State, StatesGroup


class SpendingsMenuState(StatesGroup):
    idle = State()
    add_budget = State()
    ad_spending = State()
