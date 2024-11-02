from storage import getmount
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
split = Split(
    data_pin  = keyboard.data_pin,
    use_pio   = True,
    uart_flip = True
    # data_pin2=,
)
keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

GO_LOWER = KC.MO(1)
______ = KC.TRNS

# fmt:off
keyboard.keymap = [
    # Base layer
    [
    KC.EQUAL,    KC.N1,     KC.N2,    KC.N3,    KC.N4,  KC.N5,                                    KC.N6,  KC.N7,  KC.N8,  KC.N9,   KC.N0,       KC.MINUS,
    KC.TAB,      KC.QUOTE,  KC.COMMA, KC.DOT,   KC.P,   KC.Y,                                     KC.F,   KC.G,   KC.C,   KC.R,    KC.L,        KC.SLASH,
    GO_LOWER,    KC.A,      KC.O,     KC.E,     KC.U,   KC.I,                                     KC.D,   KC.H,   KC.T,   KC.N,    KC.S,        KC.BSLASH,
    KC.LSHIFT,   KC.SCOLON, KC.Q,     KC.J,     KC.K,   KC.X,                                     KC.B,   KC.M,   KC.W,   KC.V,    KC.Z,        KC.RSHIFT,
    KC.GRAVE,    KC.ESC,    KC.LEFT,  KC.RIGHT,                                                                   KC.UP,  KC.DOWN, KC.LBRACKET, KC.RBRACKET,
                                                KC.BSPACE, KC.LCTRL,  KC.HOME,    KC.PGUP,   KC.RCTRL, KC.SPACE,
                                                KC.LALT,   KC.DELETE, KC.END,     KC.PGDOWN, KC.RCMD,  KC.ENTER,
    ],
    # Function Layer
    [
    ______,    KC.F1,     KC.F2,    KC.F3,    KC.F4,  KC.F5,                                      KC.F6,  KC.F7,  KC.F8,      KC.F9,  KC.F10,    ______,
    ______,    KC.F11,    KC.F12,   ______,   KC.MEDIA_PLAY_PAUSE, ______,                        ______, ______, KC.CAPSLOCK,______, ______,    ______,
    GO_LOWER,  ______,    ______,   ______,   ______, ______,                                     ______, ______, ______,     ______, ______,    ______,
    ______,    ______,    ______,   ______,   ______, ______,                                     ______, KC.AUDIO_MUTE,______,______,______,    ______,
    ______,    ______,    KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK,                             KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN,   ______,    ______,
                                                ______,    ______,    ______,     ______,    ______,   ______,
                                                ______,    ______,    ______,     ______,    ______,   ______,
    ]
]
# fmt:on

keyboard.debug_enabled = False


if __name__ == '__main__':
    print("Keyboard ",getmount("/").label)
    keyboard.go()
