from aiogram.dispatcher.filters.state import State, StatesGroup


class WalletState(StatesGroup):
    idle = State()
    add_wallet = State()
    remove_wallet = State()
    confirmation = State()
    choose_wallets = State()
    get_single_wallet = State()



