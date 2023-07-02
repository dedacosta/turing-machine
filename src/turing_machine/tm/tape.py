from __future__ import annotations

from turing_machine.structure import DoubleLinkedList
from turing_machine.tm.constants import Status, Direction


class Tape:
    def __init__(self) -> None:
        self.dll: DoubleLinkedList = DoubleLinkedList()
        self.dll.append(Status.START)
        self.current = self.dll.get_node_head()

    def move(self, drc: Direction) -> None:
        match drc:
            case Direction.LEFT:
                if self.current.has_prev():
                    self.current = self.current.prev()
                else:
                    raise Exception("This move is not allowed.")
            case Direction.RIGHT:
                if self.current.has_next():
                    self.current = self.current.next()
                else:
                    self.dll.append(Status.BLANK)
                    self.current = self.dll.get_node_tail()
            case Direction.HALT:
                pass

    def read(self):
        return self.current.value()

    def write(self, value) -> None:
        if self.current.value() != Status.START:
            self.current.set_value(value)

    def reset(self) -> None:
        self.dll.get_node_head()

    def input(self, s) -> None:
        for elem in s:
            if elem != '1' and elem != '0':
                raise Exception("Input is not conform.")
            tape.move(Direction.RIGHT)
            tape.write(Status.ONE if elem == '1' else Status.ZERO)
        self.current = self.dll.get_node_head()

    def output(self) -> str:
        res = ""
        node = self.dll.get_node_head()
        node = node.next()
        while node is not None:
            match (node.value()):
                case Status.ONE:
                    res += "1"
                case Status.ZERO:
                    res += "0"
                case Status.BLANK:
                    break
            node = node.next()
        return "{0}".format(res)

    def __str__(self) -> str:
        res = ""
        node = self.dll.get_node_head()
        while node is not None:
            res += str(node.value()) + ("," if node.has_next() else "")
            node = node.next()
        return "{{{0}}}".format(res)


if __name__ == "__main__":
    tape = Tape()
    tape.move(Direction.RIGHT)
    tape.write(Status.ONE)
    tape.move(Direction.RIGHT)
    tape.write(Status.ZERO)
    tape.move(Direction.RIGHT)
    tape.write(Status.ONE)
    tape.move(Direction.RIGHT)
    print(tape)
    print(tape.output())

    tape = Tape()
    tape.input("1011101010")
    print(tape)
    print(tape.output())
