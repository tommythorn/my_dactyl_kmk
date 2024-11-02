import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
board.GP28,
board.GP27,
board.GP26,
board.GP22,
board.GP20,
board.GP23,
board.GP21,
)
keyboard.row_pins = (board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# keyboard.keymap = [
#     [KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,
#      KC.H,KC.I,KC.J,KC.K,KC.L,KC.M,KC.N,
#      KC.O,KC.P,KC.Q,KC.R,KC.S,KC.T,KC.U,
#      KC.V,KC.W,KC.X,KC.Y,KC.Z,KC.MINUS,KC.EQUAL,
#      KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,
#      KC.N7,KC.N8,KC.N9,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,
#      ]
# ]

keyboard.keymap = [[
    KC.NO,		KC.N6,		KC.N7,		KC.N8,		KC.N9,		KC.N0,		KC.MINUS,
    KC.NO,		KC.F,		KC.G,		KC.C,		KC.R,		KC.L,		KC.SLASH,
    KC.NO,		KC.D,		KC.H,		KC.T,		KC.N,		KC.S,		KC.BSLASH,
    KC.NO,		KC.B,		KC.M,		KC.W,		KC.V,		KC.Z,		KC.LSHIFT,
    KC.NO,		KC.SPACE,	KC.ENTER,	KC.UP,		KC.DOWN,	KC.LBRACKET,	KC.RBRACKET,
    KC.NO,		KC.LCTRL,	KC.LCMD,	KC.PGUP,	KC.PGDOWN,	KC.N5,		KC.N6,
]]

if __name__ == '__main__':
    print("Starting keyboard")
    keyboard.go()
    
