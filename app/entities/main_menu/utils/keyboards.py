from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callbacks import main_menu_cb
from .callback_actions import *
from app.entities.wallet.utils.callbacks import wallet_cb
from app.entities.wallet.utils.callback_data import WalletProcesses, WalletActions
from app.entities.categories.utils.callbacks import category_cb
from app.entities.categories.utils.callback_data import CategoriesActions, CategoriesProcesses

main_menu_kb = InlineKeyboardMarkup(row_width=2)

wallets_btn = InlineKeyboardButton(text='Управление кошельками',
                                   callback_data=wallet_cb.new(name='', process=WalletProcesses.Base,
                                                               action=WalletActions.Start))
spendings_btn = InlineKeyboardButton(text='Доходы/расходы',
                                     callback_data=main_menu_cb.new(action=main_menu_spendings))
categories_btn = InlineKeyboardButton(text="Категории",
                                      callback_data=category_cb.new(name='', process=CategoriesProcesses.Base,
                                                                    action=CategoriesActions.Start))
main_menu_kb.add(wallets_btn, spendings_btn, categories_btn)
