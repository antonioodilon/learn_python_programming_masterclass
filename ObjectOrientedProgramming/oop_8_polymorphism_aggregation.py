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
        self.end_tag = ""


class Head(Tag):

    def __init__(self, document_title):
        self._title = Title(document_title)
        super().__init__("head", self._title)


class Title(Tag):

    def __init__(self, document_title):
        # self._document_title = document_title
        super().__init__("title", document_title)


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

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head_ = head
        self._body_ = body

    def add_tag(self, name, contents):
        self._body_.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head_.display(file=file)
        self._body_.display(file=file)
        print("</html>", file=file)


if __name__ == "__main__":
    # Using aggregation:
    new_body = Body()
    new_body.add_tag("h1", "Aggregation")
    new_body.add_tag("p", "Unlike composition, <strong>aggregation</strong>"
                          "uses existing instances of objects to build up"
                          "another object.")
    new_body.add_tag("p", "The composed object doesn't actually own the objects"
                          "that it's composed of. If destroyed, these objects"
                          "continue to exist.")
    new_docType = DocType()
    new_header = Head("Aggregation document")
    my_aggregation_page = HtmlDoc(new_docType, new_header, new_body)

    with open("oop_8_aggregation.html", "w") as aggregation_test:
        my_aggregation_page.display(file=aggregation_test)

    # Using composition:
    # antonios_page = HtmlDoc()
    # antonios_page.add_tag("h1", "Main Heading")
    # antonios_page.add_tag("h2", "Sub-heading")
    # antonios_page.add_tag("p", "This is a paragraph")
    # antonios_page.display()
