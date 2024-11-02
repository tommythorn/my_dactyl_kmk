import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP21,board.GP23,board.GP20,board.GP22,board.GP26,board.GP27,board.GP28,)
keyboard.row_pins = (board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,
     KC.H,KC.I,KC.J,KC.K,KC.L,KC.M,KC.N,
     KC.O,KC.P,KC.Q,KC.R,KC.S,KC.T,KC.U,
     KC.V,KC.W,KC.X,KC.Y,KC.Z,KC.MINUS,KC.EQUAL,
     KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,
     KC.N7,KC.N8,KC.N9,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,
     ]
]

if __name__ == '__main__':
    print("Starting keyboard")
    keyboard.go()
