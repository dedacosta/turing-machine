class Node:
    def __init__(self, value, p=None, n=None):
        self.__value = value
        self.__prev = p
        self.__next = n

    def value(self):
        return self.__value

    def set_value(self, v) -> None:
        self.__value = v

    def next(self) -> 'Node':
        return self.__next

    def prev(self) -> 'Node':
        return self.__prev

    def set_next(self, n) -> None:
        self.__next = n

    def set_prev(self, p) -> None:
        self.__prev = p

    def has_next(self) -> bool:
        return self.__next is not None

    def has_prev(self) -> bool:
        return self.__prev is not None
