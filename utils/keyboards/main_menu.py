from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.callbacks import *


main_menu_kb = InlineKeyboardMarkup(row_width=1)

wallet_menu_button = InlineKeyboardButton(
    text='Управление кошельками',
    callback_data=wallet_cb.new(
        name='',
        action="wallet_start"
    )
)

spendings_menu_button = InlineKeyboardButton(
    text='Доходы/Расходы(Coming Soon)',
    callback_data=spendings_cb.new(
        action="spendings_start"
    )
)

statistics_menu_button = InlineKeyboardButton(
    text='Статистика(Coming soon)',
    callback_data=statistics_cb.new(
        action="statistics_start"
    )
)

main_menu_kb.add(wallet_menu_button,spendings_menu_button,statistics_menu_button)




