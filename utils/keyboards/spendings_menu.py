from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.callbacks import *


spendings_menu_kb = InlineKeyboardMarkup(row_width=1)

add_budget_button = InlineKeyboardButton(
    text='Добавить доходы',
    callback_data=wallet_cb.new(
        name='',
        action="add_budget"
    )
)

add_spending_button = InlineKeyboardButton(
    text='Добавить Расходы',
    callback_data=spendings_cb.new(
        action="spendings_start"
    )
)

go_back_button = InlineKeyboardButton(
    text="Назад",
    callback_data=spendings_cb.new(
    action="spendings_go_back"
    )
)

spendings_menu_kb.add(add_budget_button,add_spending_button, go_back_button)