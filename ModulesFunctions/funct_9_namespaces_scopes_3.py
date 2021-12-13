def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more spam"  # y must exist before spam3 is called
        y += spam3()  # don't combine these assingments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"  # x must exist before spam2 is called
    x += spam2()  # do not combine the assignment on this line with the one in
    # the previous
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())
# Worth reading! https://docs.python.org/3/library/functions.html#locals