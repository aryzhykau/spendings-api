from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from bot import dp

from states.UserState import UserState
from crud.user import new_user, check_user, get_name
from crud.wallet import new_wallet
from utils.keyboards.main_menu import main_menu_kb


@dp.message_handler(commands="start", state="*")
async def cmd_start(message: Message, state: FSMContext):
    await state.finish()
    await state.reset_state()
    # создаем нового пользователя или приветствуем старого
    user_id = message.from_user.id

    if check_user(user_id):
        user_name = get_name(user_id)

        await UserState.in_menu.set()
        await message.answer(f"Привет, *{user_name}*, Пожалуйста выбери категорию действий", reply_markup=main_menu_kb)
    else:
        new_user(message.from_user.id, message.from_user.full_name)
        await UserState.first_wallet.set()
        await message.answer(f'''Привет *{message.from_user.full_name}*\\!
Добро пожаловать в бот по учету расходов\\. Я помогу тебе вести учет расходов и получать статистику\\.
Давай создадим тебе твой первый *кошелек*\\. Далее ты сможешь создавать их сколько угодно\\.
Введи пожалуйста *название* своего первого кошелька\\.
''')



@dp.message_handler(state=UserState.first_wallet)
async def create_wallet(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['walletname'] = message.text
        new_wallet(message.from_user.id, data['walletname'])
    await UserState.in_menu.set()
    await message.answer(f"Поздравляю, ты добавил кошелек {message.text}\\. Теперь можешь добавлять другие кошельки, добавлять доходы и расходы а так же смотреть статистику\\. Все действия доступны с помощью кнопок\\.", reply_markup=main_menu_kb)







