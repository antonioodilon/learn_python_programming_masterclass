def banner_text(text, banner_width=80):
    # Giving a function parameter a default value
    if len(text) > banner_width - 4:
        raise ValueError("The length of the string {0} is bigger than the "
                         "screen width {1}".format(text, banner_width))
    # Raising an exception. Not ideal, but better than causing people to
    # get hurt because of a poorly-written function
    if text == "*":
        print("*" * banner_width)
    else:
        output_string = "**{0}**".format(text.center(banner_width - 4))
        print(output_string)
    return banner_width


# The following text is just a reference to the Warhammer fantasy universe
banner_text("*", 80)
banner_text("Khorne, grant your power, that I might crush thy enemies!", 80)
banner_text(" ", 80)
banner_text("Mighty Tzeentch, no one can stand against the Raven Host!", 80)
banner_text(" ", 80)
banner_text("Nurgle's maggots are growing hungry for new enemy flesh...!", 80)
banner_text("*", 80)