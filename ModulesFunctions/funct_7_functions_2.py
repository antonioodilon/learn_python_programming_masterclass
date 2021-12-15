def centre_text(*args, sep=" ", end_char="\n", centered_file=None, flush_me=False):
    # args = a variable number of arguments. As many as you want
    text = ""
    for arg in args:
        text += str(arg) + sep
    # Since args is a tuple, we need to first iterate through the tuple using
    # a for loop, unpack it, convert each arg to a string, and then concatenate
    # with text.
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char, file=centered_file, flush=flush_me)
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    # Alternative way of writing this. Just make sure to change the names of
    # the parameters as well


centre_text("Beef liver", "Chicken breast")
centre_text("Sausages", "Bacon", "Chicken legs", "Lard")
centre_text(1, 2, "3", "4", "Five", "Six", sep="/")