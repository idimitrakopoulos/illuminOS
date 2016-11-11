import pyb

from hw.board.Board import Board


class PyBoard(Board):

    pins = {

            "X1" : pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN),

    }
