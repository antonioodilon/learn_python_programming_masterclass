# Getting part of the code from the course_remaster_1_read_text_1.py file

# If you don't explicitly tell Python that the encoding should be in utf-8,
# then the output may have strange characters, depending on the configurations
# of the user's computer.
# So make sure that you ALWAYS explicitly tell Python the encoding, so that
# the software works for ALL people!
with open('Jabberwocky.txt', encoding='utf-8') as jabber_5:
    for line in jabber_5:
        print(line.rstrip())

# Go to the Jabberwocky.txt file. If you press the UTF-8 button on the bottom
# right, you will see different encodings, and some of them will have warning
# symbols. This means that changing the encoding of that particular file will
# either change the contents of the file, or lose data. BE AWARE OF THAT!

# If you have problems reading a text file, that almost always is a problem
# with the encoding! Change to the correct encoding, and it will likely work.
