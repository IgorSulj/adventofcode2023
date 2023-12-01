import re

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
} | {str(i): i for i in range(1, 10)}

digits_re = f'{"|".join(digits.keys())}'

first_picker = re.compile(rf'^.*?({digits_re}).*$')
last_picker = re.compile(rf'^.*({digits_re}).*?$')


def calibration_code(s: str):
    first = first_picker.match(s)
    last = last_picker.match(s)
    if first is None or last is None:
        raise ValueError('Failed to find first or last digit')
    return digits[first[1]] * 10 + digits[last[1]]


def main():
    with open('data.txt') as f:
        res = sum(calibration_code(s.strip()) for s in f)
        print(res)


if __name__ == '__main__':
    main()
