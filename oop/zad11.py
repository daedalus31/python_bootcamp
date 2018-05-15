class Element:
    def render(self):
        raise NotImplementedError


class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, element: Element):
        self.elements.append(element)

    def render(self):
        return '\n'.join([el.render() for el in self.elements])


class HeaderElement(Element):
    def __init__(self, header_text):
        self.header_text = header_text

    def render(self):
        return f'# {self.header_text}'


class SimpleElement(Element):
    def __init__(self, element_text):
        self._element_text = element_text

    def render(self):
        return self._element_text


class LinkElement(Element):
    def __init__(self, link_text, url):
        self._link_text = link_text
        self._url = url

    def render(self):
        return f'({self._link_text})[{self._url}]'


def test_header():
    doc = Document()
    header_element = HeaderElement('test')
    doc.add_element(header_element)

    assert doc.render() == '# test'


def test_link():
    doc = Document()
    link_element = LinkElement('test', 'http://test.example.com')
    doc.add_element(link_element)

    assert doc.render() == '(test)[http://test.example.com]'


def test_simple():
    doc = Document()
    simple_element = SimpleElement('Test')
    doc.add_element(simple_element)

    assert doc.render() == 'Test'


def test_complex_document():
    doc = Document()
    header_element = HeaderElement('test')
    link_element = LinkElement('test', 'http://test.example.com')
    simple_element = SimpleElement('Test')
    doc.add_element(header_element)
    doc.add_element(link_element)
    doc.add_element(simple_element)

    res = doc.render()

    assert res == '# test\n(test)[http://test.example.com]\nTest'
