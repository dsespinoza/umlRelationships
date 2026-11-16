#Dependency
class Document:

    def __init__(self, content: str):
        self.content = content


class Printer:

    def print_doc(self, doc: Document):
        print(f"Printing content: {doc.content}")



printer = Printer()
doc = Document("Sample PDF Text")
printer.print_doc(doc)  