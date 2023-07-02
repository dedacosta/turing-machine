from turing_machine.structure.node import Node


class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node

    def prepend(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node

    def get_node_tail(self) -> Node:
        return self.tail

    def get_node_head(self) -> Node:
        return self.head

    def __str__(self) -> str:
        node = self.head
        res = ""
        while node is not None:
            res += "{0}{1}".format(node.value(), ", " if node.has_next() else "")
            node = node.next()
        return "{{{0}}}".format(res)

    def __len__(self) -> int:
        node = self.head
        counter = 0
        while node is not None:
            counter += 1
            node = node.next()
        return counter


if __name__ == "__main__":
    dlist = DoubleLinkedList()
    print(dlist)
    dlist.append(5)
    print(dlist)
    dlist.prepend(7)
    print(dlist)
    dlist.append(19)
    print(dlist)
    print(len(dlist))
    print(id(dlist.get_node_head()))
    print(id(dlist.get_node_tail()))
