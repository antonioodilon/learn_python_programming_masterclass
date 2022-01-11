def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + " "
    # text = "-".join(args)  # This will produce an error in the calls of the
    # function with ints
    text = "-".join([str(arg) for arg in args])
    # If we don't put the square brackets, this becomes a generator expression:
        # "-".join(str(arg) for arg in args)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")