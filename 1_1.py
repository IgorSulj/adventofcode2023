from typing import Iterable, TypeVar

T = TypeVar("T")


def get_first_last(seq: Iterable[T]) -> tuple[T, T]:
    match tuple(seq):
        case []:
            raise ValueError("Sequence must have at least one element")
        case [first, *_, last]:
            return (first, last)
        case [value]:
            return (value, value)
        case _:
            print(*seq)
            raise ValueError("Sequence must have at least one element")
    

def digits_only(s: str):
    return (int(i) for i in s if i.isdigit())


def calibration_code(s: str):
    first, last = get_first_last(digits_only(s))
    return first * 10 + last


def main():
    with open('data.txt') as f:
        res = sum(calibration_code(s) for s in f)
        print(res)


if __name__ == '__main__':
    main()
