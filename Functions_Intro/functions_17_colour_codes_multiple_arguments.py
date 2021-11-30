import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_codes(text: str, *effects: str) -> None:
    """
    :param text: The text that will be formatted.
    :param effects: The effect we want. Takes the value of zero or more of the
    constants defined at the start of this module
    :returns: None
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
colour_codes("This text is magenta.", MAGENTA)
colour_codes("This text is magenta and bold.", MAGENTA, BOLD)
colour_codes("This text is magenta, bold and underlined.", MAGENTA, BOLD,
             UNDERLINE)
colour_codes("This text is red.", RED)
colour_codes("This text is red and reversed.", REVERSE, RED)
colour_codes("...And this one is in blue", BLUE)
colorama.deinit()