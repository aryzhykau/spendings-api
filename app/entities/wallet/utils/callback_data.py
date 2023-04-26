from enum import auto
from strenum import SnakeCaseStrEnum


class WalletProcesses(SnakeCaseStrEnum):
    Base = auto()
    Creating = auto()
    Info = auto()
    Deleting = auto()


class WalletActions(SnakeCaseStrEnum):
    Start = auto()
    Create = auto()
    GetAll = auto()
    ProcessChosen = auto()
    GoBack = auto()


