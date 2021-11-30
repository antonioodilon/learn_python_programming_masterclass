def banner_text(text=" ", banner_width=80):
    # Giving a function parameter a default value. Doing the same for var text
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
banner_text("*", 70)  # The default value for banner_width is 80, but it
# can be changed if the user or developer so desires
banner_text("Khorne, grant your power, that I might crush thy enemies!", 70)
banner_text(banner_width=70, text="--Testing code--")
# Providing a keyword argument
# Notice that, when using keyword arguments, we don't need to put them in
# their default positions (when the function is defined)
banner_text("Mighty Tzeentch, no one can stand against the Raven Host!", 70)
banner_text(text="--Testing code 2--", banner_width=70)
banner_text("Nurgle's maggots are growing hungry for new enemy flesh...!", 70)
banner_text("*", 70)