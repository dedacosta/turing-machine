import json
import sys


def main(argv: list[str]) -> None:
    filename = argv[1] if len(argv) == 2 else None
    print(f"")
    ast = parser.parse(content)
    print(ast)
    print(json.dumps(ast))


if __name__ == '__main__':
    main(sys.argv)
