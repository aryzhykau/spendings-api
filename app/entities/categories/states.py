from aiogram.dispatcher.filters.state import State, StatesGroup


class CategoryState(StatesGroup):
    Idle = State()
    AddCategory = State()
    ProcessEmoji = State()
    RemoveCategory = State()
    ChooseCategory = State()
