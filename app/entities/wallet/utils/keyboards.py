from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks import wallet_cb
from callback_actions import *


wallet_menu_kb = InlineKeyboardMarkup()
wallet_create_button = InlineKeyboardButton(
    text='Добавить кошелек',
    callback_data=wallet_cb.new(
        name='',
        action=wallet_create
    )
)
wallet_delete_button = InlineKeyboardButton(
    text='Удалить кошелек',
    callback_data=wallet_cb.new(
        name='',
        action=wallet_delete
    )
)
wallet_get_all_button = InlineKeyboardButton(
    text='Получить все кошельки',
    callback_data=wallet_cb.new(
        name='',
        action=wallet_get_all
    )
)
wallet_go_back_button = InlineKeyboardButton(
    text='Назад',
    callback_data=wallet_cb.new(
        name='',
        action=wallet_go_back
    )
)

wallet_menu_kb.add(wallet_create_button, wallet_delete_button, wallet_get_all_button, wallet_go_back_button)


#1
class WalletListKeyboardMarkup(InlineKeyboardMarkup):
    def __init__(self, wallets: list, action: str):
        for wallet in wallets:
            self.add(InlineKeyboardButton(
                text=wallet,
                callback_data=wallet_cb.new(name=wallet, action=action)
            ))


#2
def create_wallet_list_kb(wallets: list, action: str):
    kb = InlineKeyboardMarkup()
    for wallet in wallets:
        kb.add(InlineKeyboardButton(
            text=wallet,
            callback_data=wallet_cb.new(name=wallet, action=action)
        ))
    return kb

