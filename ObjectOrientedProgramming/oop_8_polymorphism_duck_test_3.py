# Creating an HTML using inheritance and composition in Python. It is possible
# to use both strategies when writing code.

class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self):
        print(self)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"'
                         ' "http://www.w3.org/TR/html4/strict.dtd"', '')
        self.end_tag = ""  # Doctype doesn't have an end tag


class Head(Tag):

    def __init__(self):
        super().__init__("head", "")


class Body(Tag):

    def __init__(self):
        super().__init__("body", "")  # We will build the body contents
        # separately
        self._body_contents = []  # We will populate this list with the contents
        # that the body part of the HTML will receive

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self):  # This display method overrides the display method
        # in the Tag superclass. It iterates through the _body_contents list
        # and then adds each element to contents, which was inherited from
        # the Tag class
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display()



