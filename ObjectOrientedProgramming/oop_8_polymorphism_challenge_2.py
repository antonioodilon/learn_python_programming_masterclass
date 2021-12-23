class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self):
        print(self)

    """Junk code (part of my attempt to beat the challenge):"""
    # def _title_method(self):
    #     titlemethod = "title", "Document title"
    #     return titlemethod


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"'
                         ' "http://www.w3.org/TR/html4/strict.dtd"', '')
        self.end_tag = ""  # Doctype doesn't have an end tag


class Head(Tag):

    def __init__(self, document_title):
        self._title = Title(document_title)
        super().__init__("head", self._title)

        """Junk code (part of my attempt to beat the challenge):"""
        # self._title = Tag("title", "Document title")

    """Junk code (part of my attempt to beat the challenge):"""
    # def my_title(self, title_contents):
    #     self.title_contents = title_contents

    # def _title_method(self):
    #     super().__init__("title", "Document title")

    # def _title(self):
    #     super().__init__("title", "Document title")
    #     # self._title = Tag("title", "Document title")
    #
    # def __init__(self):  # Creating a _weapon_halberd object and assigning
    #     # it to the Halberd class.
    #     self._weapon_halberd = Halberd(3.5)


class Title(Tag):

    # def __init__(self):
    #     super().__init__("title", "Document title")
    #     super().display()

    def __init__(self, document_title):
        # self._document_title = document_title
        super().__init__("title", document_title)
        # super().display()  # If you display it, the text "The title of the
        # document will appear on the top of the output

        """Junk code (part of my attempt to beat the challenge):"""
        # super().__init__()
        # self._title_contents = Head()
        # self._title_contents.my_title("Document title")
        # super().display()


class Body(Tag):

    def __init__(self):
        super().__init__("body", "")
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display()


class HtmlDoc(object):

    def __init__(self):
        self._doc_type = DocType()
        self._head_ = Head("The title of the document is here")
        self._body_ = Body()

        """Junk code (part of my attempt to beat the challenge):"""
        # self._title_head = Title()
        # self._head._title()

    def add_tag(self, name, contents):
        self._body_.add_tag(name, contents)

    def display(self):
        self._doc_type.display()
        print("<html>")
        self._head_.display()
        self._body_.display()
        print("</html>")


if __name__ == "__main__":
    antonios_page = HtmlDoc()
    antonios_page.add_tag("h1", "Main Heading")
    antonios_page.add_tag("h2", "Sub-heading")
    antonios_page.add_tag("p", "This is a paragraph")
    antonios_page.display()

    # To write to a file:
    # with open("oop_8_html.html", "w") as oop_8_html:
    #     antonios_page.display(file=oop_8_html)