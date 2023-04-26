from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from app.bot import dp, bot
from app.entities.main_menu.states import *
from app.entities.main_menu.utils.keyboards import main_menu_kb
from . import crud
from .utils.callback_data import CategoriesActions, CategoriesProcesses
from .utils.callbacks import *
from .states import *
from .utils.keyboards import *



@dp.callback_query_handler(category_cb.filter(process=CategoriesProcesses.Base, action=CategoriesActions.Start), state="*")
async def show_category_menu(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await CategoryState.Idle.set()
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text='Меню/Категории',
                                reply_markup=category_menu_kb)


############# category creation ####################

@dp.callback_query_handler(category_cb.filter(process=CategoriesProcesses.Creating, action=CategoriesActions.NamePrompt), state="*")
async def create_category(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await CategoryState.AddCategory.set()
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text='Введи название категории')


@dp.message_handler(state=CategoryState.AddCategory)
async def process_create_category(message: Message, state: FSMContext):
    if crud.check_category(message.text):
        await bot.send_message(chat_id=message.from_user.id, text="Такая категория уже есть",
                               reply_markup=category_menu_kb)
        await state.finish()
        await CategoryState.Idle.set()
    else:
        category = message.text
        emoji_promt_kb = AddEmojiInlineKeyboardMarkup(process=CategoriesProcesses.Creating, action=CategoriesActions.Save)
        await bot.send_message(chat_id=message.from_user.id, text="Прикрепляем эмодзи к категории?", reply_markup=emoji_promt_kb)
        await state.update_data({'category_name': category})
        await CategoryState.ProcessEmoji.set()

@dp.callback_query_handler(category_cb.filter(action=CategoriesActions.EmojiAddPrompt), state=CategoryState.ProcessEmoji)
async def process_emoji_creation(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text='Введи эмодзи для категории')

@dp.callback_query_handler(category_cb.filter(action=CategoriesActions.Save), state=CategoryState.ProcessEmoji)
async def proccess_without_emoji(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    state_data = await state.get_data()
    category_name = state_data['category_name']
    category_emoji = ''
    crud.create_category(callback.from_user.id, category_name, category_emoji)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text=f"Категория {category_emoji}{category_name}{category_emoji} создана ",
                                reply_markup=category_menu_kb)
    await state.finish()
    await CategoryState.Idle.set()



@dp.message_handler(state=CategoryState.ProcessEmoji)
async def save_category(message: Message, state: FSMContext):
    state_data = await state.get_data()
    category_name = state_data['category_name']
    category_emoji = message.text
    crud.create_category(message.from_user.id, category_name, category_emoji)
    await bot.send_message(chat_id=message.from_user.id, text=f"Категория {category_emoji}{category_name}{category_emoji} создана ", reply_markup=category_menu_kb)
    await state.finish()
    await CategoryState.Idle.set()



################ categories list ######################

@dp.callback_query_handler(category_cb.filter(action=CategoriesActions.GetAll), state='*')
async def get_all_categories_list(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    print('start')
    await CategoryState.ChooseCategory.set()
    categories = crud.get_all_user_categories(callback.from_user.id)
    categories_list_kb = CategoriesListKeyboardMarkup(categories=categories,
                                                      process=CategoriesProcesses.Info,
                                                      action=CategoriesActions.ProcessChosen)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text='Список категорий', reply_markup=categories_list_kb)



@dp.callback_query_handler(category_cb.filter(action=CategoriesActions.GoBack), state='*')
async def go_back(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    if callback_data['process'] == CategoriesProcesses.Base:
        await MainMenuState.idle.set()
        await state.finish()
        await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id, text="Меню",
                                    reply_markup=main_menu_kb)
    else:
        await CategoryState.Idle.set()
        await state.finish()
        await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                    text='Меню/Категории', reply_markup=category_menu_kb)










