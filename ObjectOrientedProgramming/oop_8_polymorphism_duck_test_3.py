# Creating an HTML using inheritance and composition in Python. It is possible
# to use both strategies when writing code.

# is a = inheritance
# For example, DocType IS A Tag, Head IS A Tag, and Body IS A Tag. This is
# a good indication that we should use inheritance instead of composition.

# has a = composition
# For example, in the class Body there is and add_tag method that HAS A
# reference to the Tag class (new_tag = Tag(name, contents)). This is a good
# indication that we should use composition.


class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


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

    def display(self, file=None):  # This display method overrides the display method
        # in the Tag superclass. It iterates through the _body_contents list
        # and then adds each element to contents, which was inherited from
        # the Tag class
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


# Composition doesn't mean that a class is entirely made out of other classes.
# It just means that a class contains other classes, but it can also be its
# own thing. Our Html class contains other classes, and can make use of the
# attributes that other classes provide, but it can have its own methods etc.
class HtmlDoc(object):

    def __init__(self):
        self._doc_type = DocType()
        self._head_ = Head()
        self._body_ = Body()

    def add_tag(self, name, contents):
        self._body_.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head_.display(file=file)
        self._body_.display(file=file)
        print("</html>", file=file)


if __name__ == "__main__":
    antonios_page = HtmlDoc()
    antonios_page.add_tag("h1", "Main Heading")
    antonios_page.add_tag("h2", "Sub-heading")
    antonios_page.add_tag("p", "This is a paragraph")
    # Creating an html file that can be opened in browser:
    with open("oop_8_html.html", "w") as oop_8_html:
        antonios_page.display(file=oop_8_html)

