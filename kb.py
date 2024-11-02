from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
import board

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9)
    col_pins = (board.GP28, board.GP27, board.GP26, board.GP22, board.GP20, board.GP23, board.GP21)
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.GP3

    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,  5,      43, 44, 45, 46, 47, 48,      
         7,  8,  9, 10, 11, 12,      50, 51, 52, 53, 54, 55,
        14, 15, 16, 17, 18, 19,      57, 58, 59, 60, 61, 62,
        21, 22, 23, 24, 25, 26,      64, 65, 66, 67, 68, 69,
        28, 29, 30, 31,                      73, 74, 75, 76,
                       33, 40, 38,   80, 78, 71,
                       32, 39, 37,   81, 79, 72,

    ]
    # fmt: on
