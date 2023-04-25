from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callbacks import main_menu_cb
from .callback_actions import *
from app.entities.wallet.utils.callbacks import wallet_cb
from app.entities.wallet.utils.callback_actions import wallet_start

main_menu_kb = InlineKeyboardMarkup()

wallets_btn = InlineKeyboardButton(text='Управление кошельками',
                                   callback_data=wallet_cb.new(name='', next_action='', action=wallet_start))
spendings_btn = InlineKeyboardButton(text='Доходы/расходы',
                                     callback_data=main_menu_cb.new(action=main_menu_spendings))
main_menu_kb.add(wallets_btn, spendings_btn)
