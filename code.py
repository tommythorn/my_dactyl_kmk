from storage import getmount
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split

keyboard = KMKKeyboard()

split = Split(
    data_pin  = keyboard.data_pin,
    use_pio   = True,
    uart_flip = True
    # data_pin2=,
)
keyboard.modules.append(split)

# fmt:off
keyboard.keymap = [[
    KC.EQUAL,    KC.N1,     KC.N2,    KC.N3,    KC.N4,  KC.N5,                                    KC.N6,  KC.N7,  KC.N8,  KC.N9,   KC.N0,       KC.MINUS,
    KC.TAB,      KC.QUOTE,  KC.COMMA, KC.DOT,   KC.P,   KC.Y,                                     KC.F,   KC.G,   KC.C,   KC.R,    KC.L,        KC.SLASH,
    KC.CAPSLOCK, KC.A,      KC.O,     KC.E,     KC.U,   KC.I,                                     KC.D,   KC.H,   KC.T,   KC.N,    KC.S,        KC.BSLASH,
    KC.LSHIFT,   KC.SCOLON, KC.Q,     KC.J,     KC.K,   KC.X,                                     KC.B,   KC.M,   KC.W,   KC.V,    KC.Z,        KC.RSHIFT,
    KC.GRAVE,    KC.ESC,    KC.LEFT,  KC.RIGHT,                                                                   KC.UP,  KC.DOWN, KC.LBRACKET, KC.RBRACKET,
                                                KC.BSPACE, KC.LCTRL, KC.HOME,     KC.PGUP,   KC.RCTRL, KC.SPACE,
                                                KC.LALT,   KC.DELETE, KC.END,     KC.PGDOWN, KC.RCMD,  KC.ENTER,
]]       
# fmt:on

keyboard.debug_enabled = False

if __name__ == '__main__':
    print("Keyboard ",getmount("/").label)
    keyboard.go()
