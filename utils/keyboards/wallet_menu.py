from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.callbacks import wallet_cb




wallet_menu_kb = InlineKeyboardMarkup(row_width=1)
wallet_create_button = InlineKeyboardButton(
    text='Добавить кошелек',
    callback_data=wallet_cb.new(
        name='',
        action="wallet_create"
    )
)
wallet_delete_button = InlineKeyboardButton(
    text='Удалить кошелек',
    callback_data=wallet_cb.new(
        name='',
        action="wallet_delete"
    )
)
wallet_get_all_button = InlineKeyboardButton(
    text='Получить все кошельки',
    callback_data=wallet_cb.new(
        name='',
        action="wallet_get_all"
    )
)
wallet_go_back_button = InlineKeyboardButton(
    text='Назад',
    callback_data=wallet_cb.new(
        name='',
        action="wallet_go_back"
    )
)

wallet_menu_kb.add(wallet_create_button,wallet_delete_button,wallet_get_all_button,wallet_go_back_button)