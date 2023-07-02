import enum


class Status(enum.Enum):
    START, BLANK, ZERO, ONE = range(4)


class Direction(enum.Enum):
    LEFT, RIGHT, HALT = range(3)
