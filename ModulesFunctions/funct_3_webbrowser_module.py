import webbrowser

# This class is a tour on how to read the documentation and how to use
# different modules and functions based on their documentation

# webbrowser.open("https://www.python.org/")
# To open a web page

help(webbrowser)

for i in range(10):
    print(1, 2, 3, 4, 5, sep=", ", end=". \n")  # A function often can take
    # several arguments

windows_default = webbrowser.get(using="windows-default")
windows_default.open_new("https://www.python.org/jobs/")
# See: https://docs.python.org/3.4/library/webbrowser.html