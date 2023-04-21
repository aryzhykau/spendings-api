from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from bot import dp, bot
from crud.wallet import new_wallet, get_all_wallets, get_balance, remove_wallet, get_all_wallets_names
from crud.spendings import add_balance
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from states.UserState import UserState
from states.SpendingsState import SpendingsMenuState
from utils.callbacks import spendings_cb
from utils.keyboards.spendings_menu import spendings_menu_kb
from utils.keyboards.main_menu import main_menu_kb


@dp.callback_query_handler(spendings_cb.filter(action="spendings_start"), state="*")
async def show_spendings_menu(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    print("accepted")
    await bot.answer_callback_query(callback.id)
    await SpendingsMenuState.idle.set()
    menu_message_id = callback.message.message_id
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=menu_message_id, reply_markup=spendings_menu_kb)

#adding budgets
@dp.callback_query_handler(spendings_cb.filter(action="add_budget"), state=SpendingsMenuState.add_budget)
async def add_budget(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await SpendingsMenuState.add_budget.set()
    reply_text = "Для добавления дохода выбери кошелек"
    wallets = get_all_wallets_names(callback.from_user.id)

    bot.edit_message_text(chat_id=callback.from_user.id, mesage_id=callback.message.message_id, text=reply_text)


@dp.callback_query_handler(spendings_cb.filter(action="spendings_go_back"), state="*")
async def spendings_go_back(callback: CallbackQuery, callback_data: dict):
    await UserState.in_menu.set()
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Меню", reply_markup=main_menu_kb)


