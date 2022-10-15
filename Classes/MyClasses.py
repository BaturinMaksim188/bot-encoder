from aiogram.dispatcher.filters.state import State, StatesGroup


# Class of fundamental states
class States(StatesGroup):
    CHOICE_W = State()
    CHOICE_v1 = State()
    CHOICE_v2 = State()
