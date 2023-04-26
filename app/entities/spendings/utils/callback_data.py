from strenum import SnakeCaseStrEnum
from enum import auto


class SpendingsActions(SnakeCaseStrEnum):
    Start = auto()
    Add = auto()
    ProcessChosen = auto()
    GoBack = auto()

class SpendingsProcesses(SnakeCaseStrEnum):
    Base = auto()
    Add = auto()




