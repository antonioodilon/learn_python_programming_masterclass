def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:......,,{0}, {1}".format(p1, p2))
    print("var-positional (*args packed):........{}".format(args))
    # Python printed all the values in a tuple
    print("var-positional (*args unpacked):.....{}".format(*args))
    # Python only printed the first value
    print("keyword:.................................{}".format(k))
    print("var-keyword.........................{}".format(kwargs))
    print("var-keyword........................{}".format(*kwargs))


func(1, 2, 3, 4, 5, 6, k=7, key1=8, key2=9, key3=10, key4=11)
