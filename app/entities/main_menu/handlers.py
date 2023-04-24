from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from app.bot import dp, bot
from app.entities.categories.base import *
from crud import *
from states import *
from utils.keyboards import *


@dp.message_handler(commands='start')
async def process_start(message: Message, state: FSMContext):
    await MainMenuState.welcome.set()
    new_user = create_user(
        telegram_id=message.from_user.id,
        name=message.from_user.full_name,
        base_categories=base_categories
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в бот для ведения расходов, давай создадим твой первый кошелек. Введи название своего кошелька")
    await MainMenuState.first_wallet.set()


@dp.message_handler(state=MainMenuState.first_wallet)
async def process_first_wallet(message: Message, state: FSMContext):
    wallet_name = message.text
    create_first_wallet(telegram_id=message.from_user.id, name=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Твой кошелек создан\\. Для управления финансами можешь воспользоваться меню",
        reply_markup=main_menu_kb
    )
    await MainMenuState.idle.set()

