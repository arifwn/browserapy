import typing


class Node:
    nodeName: str
    nodeType: int
    nodeValue: typing.Any
    childNodes: typing.List['Node']
    parentNode: 'Node'
    parentElement: 'Element'

    @property
    def textContent(self, value=None) -> str:
        pass
    
    @property
    def isConnected(self) -> bool:
        pass

    @property
    def ownerDocument(self) -> typing.Union['Document', None]:
        pass
    


class Document(Node):
    @property
    def ownerDocument(self) -> typing.Union['Document', None]:
        return None


class Element(Node):
    id: str
    className: str
    children: typing.List['Element']
    
    @property
    def outerHTML(self, value=None) -> typing.Union[str, None]:
        pass

    @property
    def innerHTML(self, value=None) -> typing.Union[str, None]:
        pass


class HTMLElement(Element):
    title: str
    
    @property
    def innerText(self) -> str:
        pass
