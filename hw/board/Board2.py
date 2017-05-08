import lib.toolkit as tk
from lib.toolkit import log


class Board:
    pin_mapping = []
    button_click_counter = {}

    # @timed_function
    def __init__(self, pin_mapping):
        self.pin_mapping = pin_mapping

