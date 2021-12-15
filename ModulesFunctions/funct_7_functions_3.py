# Line of code that was deleted:
# def centre_text(*args, sep=" ", end="\n", file=None, flush=False):


def centre_text(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = str(text)
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    # We used the above line of code to write the file centre_text


with open("menu", "w") as menu:
    s1 = centre_text("Beef liver", "Chicken breast")
    s2 = centre_text("Sausages", "Bacon", "Chicken legs", "Lard")
    print(s1, file=menu)
    print(s2, file=menu)
    print(centre_text(1, 2, "3", "4", "Five", "Six", sep="://"), file=menu)

# Now that the centre_text file has been created, we can comment out the
# lines of code below:
# with open("centre_text", "w") as centre_text_file:
#     centre_text("Beef liver", "Chicken breast", file=centre_text_file)
#     centre_text("Sausages", "Bacon", "Chicken legs", "Lard", file=centre_text_file)
#     centre_text(1, 2, "3", "4", "Five", "Six", file=centre_text_file)