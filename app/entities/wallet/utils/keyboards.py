from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callbacks import wallet_cb
from . import callback_actions as actions
from app.entities.main_menu.utils.callback_actions import *


wallet_menu_kb = InlineKeyboardMarkup(row_width=1)
wallet_create_button = InlineKeyboardButton(
    text='Добавить кошелек',
    callback_data=wallet_cb.new(
        name='',
        next_action='',
        action=actions.wallet_create
    )
)
wallet_delete_button = InlineKeyboardButton(
    text='Удалить кошелек',
    callback_data=wallet_cb.new(
        name='',
        next_action=actions.wallet_delete_choose,
        action=actions.wallet_get_all
    )
)
wallet_get_single_button = InlineKeyboardButton(
    text='Получить информацию о кошельке',
    callback_data=wallet_cb.new(
        name='',
        next_action=actions.wallet_get_single,
        action=actions.wallet_get_all
    )
)
wallet_go_back_button = InlineKeyboardButton(
    text='Назад',
    callback_data=wallet_cb.new(
        name='',
        next_action='',
        action=actions.wallet_main_go_back
    )
)

wallet_menu_kb.add(wallet_create_button, wallet_delete_button, wallet_get_single_button,
                   wallet_go_back_button)


#1
class WalletListKeyboardMarkup(InlineKeyboardMarkup):
    def __init__(self, wallets: list, action: str):
        super().__init__()
        for wallet in wallets:
            self.add(InlineKeyboardButton(
                text=wallet,
                callback_data=wallet_cb.new(name=wallet, next_action='', action=action)
            ))
        self.add(InlineKeyboardButton(
            text = "Назад",
            callback_data=wallet_cb.new(name='', next_action='', action=actions.go_to_wallet_menu)
        ))
