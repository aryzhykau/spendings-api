from aiogram.dispatcher.filters.state import State, StatesGroup


class SpendingsState(StatesGroup):
    Idle = State()
    AddSpending = State()
    AddBudget = State()