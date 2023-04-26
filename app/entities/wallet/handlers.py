from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from app.bot import dp, bot
from app.entities.main_menu.states import *
from app.entities.main_menu.utils.keyboards import main_menu_kb
from . import crud
from .utils.callback_data import WalletActions, WalletProcesses
from .utils.callbacks import *
from .states import *
from .utils.keyboards import *


@dp.callback_query_handler(wallet_cb.filter(process=WalletProcesses.Base, action=WalletActions.Start), state="*")
async def show_wallet_menu(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await WalletState.idle.set()
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text='Меню/Кошельки',
                                reply_markup=wallet_menu_kb)


@dp.callback_query_handler(wallet_cb.filter(action=WalletActions.GoBack), state="*")
async def wallet_go_back(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    if callback_data['process'] == WalletProcesses.Base:
        await MainMenuState.idle.set()
        await state.finish()
        await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Меню",
                                    reply_markup=main_menu_kb)
    else:
        await WalletState.idle.set()
        await state.finish()
        await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                    text='Меню/Кошельки', reply_markup=wallet_menu_kb)


################# Wallet creation ##########################################
@dp.callback_query_handler(wallet_cb.filter(process=WalletProcesses.Creating, action=WalletActions.Create), state='*')
async def wallet_create(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await WalletState.add_wallet.set()
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text="Введи название нового кошелька")

@dp.message_handler(state=WalletState.add_wallet)
async def new_wallet_name_process(message: Message, state: FSMContext):
    if crud.check_wallet(user_id=message.from_user.id, wallet_name=message.text):
        await bot.send_message(chat_id=message.from_user.id, text="Такой кошелек уже есть", reply_markup=wallet_menu_kb)
        await WalletState.idle.set()
    else:
        crud.new_wallet(user_id=message.from_user.id, wallet_name=message.text)
        await bot.send_message(chat_id=message.from_user.id, text="Кошелек создан", reply_markup=wallet_menu_kb)
        await WalletState.idle.set()


@dp.callback_query_handler(wallet_cb.filter(action=WalletActions.GetAll), state='*')
async def get_all_wallets_names(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await WalletState.choose_wallets.set()
    process = callback_data['process']
    wallets = crud.get_all_wallets_names(user_id=callback.from_user.id)
    wallets_list_kb = WalletListKeyboardMarkup(wallets, process=process, action=WalletActions.ProcessChosen)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text="Выбери кошелек", reply_markup=wallets_list_kb)


############### Getting wallet information ######################################
@dp.callback_query_handler(wallet_cb.filter(process=WalletProcesses.Info,
                                            action=WalletActions.ProcessChosen),
                           state=WalletState.choose_wallets)
async def process_single_wallet_choose(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await WalletState.get_single_wallet.set()
    wallet = crud.get_balance(user_id=callback.from_user.id, wallet_name=callback_data['name'])
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text=f"Кошелек: {wallet['name']}\n Баланс: {wallet['balance']}",
                                reply_markup=wallet_menu_kb)
    await state.finish()
    await WalletState.idle.set()


######################## Delete Wallet ######################
@dp.callback_query_handler(wallet_cb.filter(process=WalletProcesses.Deleting,
                                            action=WalletActions.ProcessChosen),
                           state=WalletState.choose_wallets)
async def process_delete_wallet(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await WalletState.remove_wallet.set()
    crud.remove_wallet(user_id=callback.from_user.id, wallet_name=callback_data['name'])
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text=f"Кошелек был удален",
                                reply_markup=wallet_menu_kb)
    await state.finish()
    await WalletState.idle.set()
