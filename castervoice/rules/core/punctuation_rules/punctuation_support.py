import dragonfly


def double_text_punc_dict():
    return {
        "quotes":                            "\"\"",
        "thin quotes":                         "''",
        "tickris":                             "``",
        "pair":                             "()",
        "brax":                                "[]",
        "curly":                               "{}",
        "angle":                               "<>",
    }


def _inv_dtpb():
    return {v: k for k, v in double_text_punc_dict().items()}


def text_punc_dict():
    # Insurers comma is recognized consistently with DNS/Natlink and
    # if/else statement workaround engines that do not expect punctuation symbol as a command
    if hasattr(dragonfly.get_current_engine(), "name"):
        if (dragonfly.get_current_engine().name == 'natlink'):
            comma = "(comma | ,)"
        else:
            comma = "comma"
    else:
        comma = "comma"

    _id = _inv_dtpb()
    return {
        "ace":                                                " ",
        "clamor":                                             "!",
        "chocky":                                            "\"",
        "hash tag":                                           "#",
        "Dolly":                                              "$",
        "modulo":                                             "%",
        "ampersand":                                          "&",
        "apostrophe | single quote | chicky":                 "'",
        "open " + _id["()"]:                                  "(",
        "close " + _id["()"]:                                 ")",
        "starling":                                           "*",
        "plus":                                               "+",
        comma:                                                ",",
        "minus":                                              "-",
        "period | dot":                                       ".",
        "slash":                                              "/",
        "deckle":                                             ":",
        "semper":                                             ";",
        "[is] less than | left " + _id["<>"]:                 "<",
        "[is] less [than] [or] equal [to]":                  "<=",
        "equals":                                             "=",
        "[is] equal to":                                     "==",
        "[is] greater than | right " + _id["<>"]:             ">",
        "[is] greater [than] [or] equal [to]":               ">=",
        "questo":                                             "?",
        "(atty | at symbol)":                                 "@",
        "open " + _id["[]"]:                                  "[",
        "backslash":                                         "\\",
        "close " + _id["[]"]:                                 "]",
        "carrot":                                             "^",
        "underscore":                                         "_",
        "ticky | ((left | right) " + _id["``"] + " )":        "`",
        "open " + _id["{}"]:                                  "{",
        "pipe (sim | symbol)":                                "|",
        "close " + _id["{}"]:                                 "}",
        "tilde":                                              "~",
    }
