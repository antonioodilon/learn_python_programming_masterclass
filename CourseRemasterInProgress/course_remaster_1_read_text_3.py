# Creating functions have behave like removesuffix and removeprefix


def my_removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def my_removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'
with open(filename) as jabber:
    line_1 = jabber.readline().rstrip()  # readline() reads one line at a time,
    # and using the rstrip() method we strip everything to the right of the
    # first line
print(line_1)

print('=' * 80)

twas_removed = my_removeprefix(line_1, "'Twas")
print(twas_removed)
toves_removed = my_removesuffix(line_1, "toves")
print(toves_removed)