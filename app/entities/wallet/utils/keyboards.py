from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callbacks import wallet_cb
from .callback_data import WalletActions, WalletProcesses
from app.entities.main_menu.utils.callback_actions import *


wallet_menu_kb = InlineKeyboardMarkup(row_width=1)
wallet_create_button = InlineKeyboardButton(
    text='Добавить кошелек',
    callback_data=wallet_cb.new(
        name='',
        process=WalletProcesses.Creating,
        action=WalletActions.Create
    )
)
wallet_delete_button = InlineKeyboardButton(
    text='Удалить кошелек',
    callback_data=wallet_cb.new(
        name='',
        process=WalletProcesses.Deleting,
        action=WalletActions.GetAll
    )
)
wallet_get_single_button = InlineKeyboardButton(
    text='Получить информацию о кошельке',
    callback_data=wallet_cb.new(
        name='',
        process=WalletProcesses.Info,
        action=WalletActions.GetAll
    )
)
wallet_go_back_button = InlineKeyboardButton(
    text='Назад',
    callback_data=wallet_cb.new(
        name='',
        process=WalletProcesses.Base,
        action=WalletActions.GoBack
    )
)

wallet_menu_kb.add(wallet_create_button, wallet_delete_button, wallet_get_single_button,
                   wallet_go_back_button)


#1
class WalletListKeyboardMarkup(InlineKeyboardMarkup):
    def __init__(self, wallets: list, process: str, action: str):
        super().__init__()
        for wallet in wallets:
            self.add(InlineKeyboardButton(
                text=wallet['name'],
                callback_data=wallet_cb.new(name=str(wallet['_id']), process=process, action=action)
            ))
        self.add(InlineKeyboardButton(
            text="Назад",
            callback_data=wallet_cb.new(name='', process=process, action=WalletActions.GoBack)
        ))
