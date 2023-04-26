from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callbacks import category_cb
from .callback_data import CategoriesActions, CategoriesProcesses
from app.entities.main_menu.utils.callback_actions import *
from strenum import  StrEnum


class CategoryMenuButtons(StrEnum):
    Create = 'Добавить категорию'
    CreateSub = 'Добавить подкатегорию'
    GetSingle = 'Мои категории'
    GoBack = 'Назад'
    Approve = 'Да'
    Decline = 'Нет'


category_menu_kb = InlineKeyboardMarkup(row_width=1)
category_create_button = InlineKeyboardButton(
    text=CategoryMenuButtons.Create,
    callback_data=category_cb.new(
        name='',
        process=CategoriesProcesses.Creating,
        action=CategoriesActions.NamePrompt
    )
)
# subcategory_create_button = InlineKeyboardButton(
#     text=CategoryMenuButtons.CreateSub,
#     callback_data=category_cb.new(
#         name='',
#         process=CategoriesProcesses.CreatingSub,
#         action=CategoriesActions.GetAll
#     )
# )
category_get_single_button = InlineKeyboardButton(
    text=CategoryMenuButtons.GetSingle,
    callback_data=category_cb.new(
        name='',
        process=CategoriesProcesses.Info,
        action=CategoriesActions.GetAll
    )
)
category_go_back_button = InlineKeyboardButton(
    text=CategoryMenuButtons.GoBack,
    callback_data=category_cb.new(
        name='',
        process=CategoriesProcesses.Base,
        action=CategoriesActions.GoBack
    )
)

category_menu_kb.add(category_create_button, category_get_single_button,
                     category_go_back_button)


class CategoriesListKeyboardMarkup(InlineKeyboardMarkup):
    def __init__(self, categories: list, process: str, action: str):
        super().__init__(row_width=3)

        for category in categories:
            self.add(InlineKeyboardButton(
                text=f"{category['emoji']}{category['name']}{category['emoji']}",
                callback_data=category_cb.new(name=category['_id'], process=process, action=action)
            ))
        self.add(InlineKeyboardButton(
            text=CategoryMenuButtons.GoBack,
            callback_data=category_cb.new(name='', process=process, action=CategoriesActions.GoBack)
        ))


class AddEmojiInlineKeyboardMarkup(InlineKeyboardMarkup):
    def __init__(self, process: str, action: str):
        super().__init__()
        self.add(InlineKeyboardButton(
            text=CategoryMenuButtons.Approve, callback_data=category_cb.new(name='', process=process, action=CategoriesActions.EmojiAddPrompt)
        ))
        self.add(InlineKeyboardButton(
            text=CategoryMenuButtons.Decline, callback_data=category_cb.new(name='', process=process, action=action)
        ))
