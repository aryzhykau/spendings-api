from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from app.bot import dp, bot
from app.entities.main_menu.states import *
from app.entities.main_menu.utils.keyboards import main_menu_kb
from . import crud
from .utils.callback_data import SpendingsActions, SpendingsProcesses
from .utils.callbacks import *
from .states import *
from .utils.keyboards import *


@dp.callback_query_handler(spending_cb.filter(process=SpendingsProcesses.Base, action=SpendingsActions.Start), state="*")
async def show_wallet_menu(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await WalletState.idle.set()
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text='Меню/Кошельки',
                                reply_markup=wallet_menu_kb)