from enum import auto
from strenum import SnakeCaseStrEnum


class CategoriesProcesses(SnakeCaseStrEnum):
    Base = auto()
    Creating = auto()
    Info = auto()
    CreatingSub = auto()


class CategoriesActions(SnakeCaseStrEnum):
    EmojiAddPrompt = auto()
    Start = auto()
    NamePrompt = auto()
    Save = auto()
    SubCreate = auto()
    GetAll = auto()
    ProcessChosen = auto()
    GoBack = auto()