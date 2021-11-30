def banner_text(text):
    screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError("The length of the string {0} is bigger than the "
                         "screen width {1}".format(text, screen_width))
# Raising an exception. Not ideal, but better than causing people to
# get hurt because of a poorly-written function
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


# The following text is just a reference to the Warhammer fantasy universe
banner_text("*")
banner_text("Khorne, grant your power, that I might crush thy enemies!")
banner_text(" ")
banner_text("Mighty Tzeentch, no one can stand against the Raven Host!")
banner_text(" ")
banner_text("Nurgle's maggots are growing hungry for new enemy flesh...!")
banner_text("*")