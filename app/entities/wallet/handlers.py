# from aiogram.dispatcher import FSMContext
# from aiogram.types import Message, CallbackQuery
# from app.bot import dp, bot
#
# from utils.callback_actions import *
#
#
# @dp.callback_query_handler(wallet_cb.filter(action="wallet_start"), state="*")
# async def show_wallet_menu(callback: CallbackQuery, callback_data: dict, state: FSMContext):
#     await bot.answer_callback_query(callback.id)
#     await WalletMenuState.idle.set()
#     menu_message_id = callback.message.message_id
#     await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=menu_message_id, reply_markup=wallet_menu_kb)
#
# # Wallet creation
# @dp.callback_query_handler(wallet_cb.filter(action="wallet_create"), state="*")
# async def cmd_create_wallet(callback: CallbackQuery, callback_data: dict, state: FSMContext):
#     await bot.answer_callback_query(callback.id)
#     user_id = callback.from_user.id
#     if check_user(user_id):
#         await WalletMenuState.create.set()
#         await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Добавим кошелек, введите название кошелька")
#     else:
#         UserState.in_menu.set()
#         await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Вы не зарегистрированы")
#
#
# @dp.message_handler(state=WalletMenuState.create)
# async def create_wallet(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     wallets = get_all_wallets_names(user_id)
#     if message.text not in wallets:
#         new_wallet(user_id, message.text)
#         await WalletMenuState.idle.set()
#         await message.answer(f"Кошелек {message.text} создан", reply_markup=wallet_menu_kb)
#
#     else:
#         await WalletMenuState.idle.set()
#         await message.answer(f"Такой кошелек уже есть", reply_markup=wallet_menu_kb)
#
#
# #Getting all wallets
# @dp.callback_query_handler(wallet_cb.filter(action="wallet_get_all"), state="*")
# async def cmd_get_all_wallets(callback: CallbackQuery, callback_data: dict, state: FSMContext):
#     await bot.answer_callback_query(callback.id)
#     await WalletMenuState.get_all.set()
#     wallets = get_all_wallets(callback.from_user.id)
#     reply_text = "Ваши кошельки:"
#     for wallet in wallets:
#         reply_text = reply_text+f"\n\\- *{wallet['name']}*: {wallet['balance']}"
#     await  bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text=reply_text, reply_markup=wallet_menu_kb)
#     await WalletMenuState.idle.set()
#     # await bot.send_message(chat_id=callback.from_user.id, text="Меню", reply_markup=wallet_menu_kb)
#
#
#
#
#
#
#
# @dp.message_handler(commands="get_balance")
# async def cmd_get_balance(message: Message):
#     user_id = message.from_user.id
#     ikb = InlineKeyboardMarkup(row_width=2)
#     if check_user(user_id):
#         user_name = get_name(user_id)
#         user_wallets = get_all_wallets(user_id)
#
#         for wallet in user_wallets:
#
#             ikb.add(InlineKeyboardButton(
#                 text=wallet["name"],
#                 callback_data=wallet_cb.new(name=wallet["name"], action="get_wallet")
#             ))
#         await message.answer(f"Привет, {user_name}, выбери кошелек", reply_markup=ikb)
#     else:
#         await message.answer(f"Вы не зарегистрированы")
#
#
#
# @dp.callback_query_handler(wallet_cb.filter(action="get_wallet"))
# async def get_wallet_balance(callback: CallbackQuery, callback_data: dict):
#     await bot.answer_callback_query(callback.id)
#     wallet_name = callback_data["name"]
#     if get_all_wallets_names(callback.from_user.id):
#         balance = get_balance(callback.from_user.id, wallet_name)
#         await bot.send_message(chat_id= callback.from_user.id ,text = f'На балансе кошелька {wallet_name} находится {balance}')
#     else:
#         await bot.send_message(chat_id= callback.from_user.id ,text = f'У тебя нет кошельков воспользуйся командой /create_wallet')
#
#
# #removing wallet
# @dp.callback_query_handler(wallet_cb.filter(action="wallet_delete"), state="*")
# async def cmd_rmv_wallet(callback: CallbackQuery, callback_data: dict, state: FSMContext):
#     user_id = callback.from_user.id
#
#     if check_user(user_id):
#         user_wallets = get_all_wallets(user_id)
#         if user_wallets:
#             ikb = InlineKeyboardMarkup(row_width=1)
#             await WalletMenuState.remove.set()
#             for wallet in user_wallets:
#                 ikb.add(InlineKeyboardButton(
#                     text=wallet["name"],
#                     callback_data=wallet_cb.new(name=wallet["name"], action="rmv_wallet")
#                 ))
#             await bot.edit_message_text(chat_id=user_id, message_id=callback.message.message_id, text="Выберите кошелек для удаления")
#             await bot.edit_message_reply_markup(chat_id=user_id, message_id=callback.message.message_id, reply_markup=ikb)
#         else:
#             await bot.send_message(chat_id=user_id, text="У вас нет кошельков\\.", reply_markup=wallet_menu_kb)
#     else:
#         await bot.send_message(chat_id=user_id, text="Вы не зарегистрированы, воспользуйтесь командой /start")
#
#
# @dp.callback_query_handler(wallet_cb.filter(action="rmv_wallet"), state="*")
# async def rmv_wallet(callback: CallbackQuery, callback_data: dict):
#     await bot.answer_callback_query(callback.id)
#     wallet_name = callback_data["name"]
#     remove_wallet(callback.from_user.id, wallet_name)
#     await WalletMenuState.idle.set()
#     await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Кошелек был удален\\.", reply_markup=wallet_menu_kb)
#
#
# @dp.callback_query_handler(wallet_cb.filter(action="wallet_go_back"), state="*")
# async def wallet_go_back(callback: CallbackQuery, callback_data: dict):
#     await UserState.in_menu.set()
#     await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Меню", reply_markup=main_menu_kb)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
