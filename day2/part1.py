from dataclasses import dataclass


@dataclass
class Round:
    blue: int = 0
    green: int = 0
    red: int = 0

    @staticmethod
    def parse(s: str):
        color_strs = map(str.strip, s.split(','))
        round_dict = {}
        for color_str in color_strs:
            count, color = color_str.split()
            round_dict[color] = int(count)
        return Round(**round_dict)

    def is_possible(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14


@dataclass
class Game:
    n: int
    rounds: list[Round]

    @staticmethod
    def parse(line: str):
        game_str, rounds_str = line.split(':', 1)
        n = int(game_str.split()[1])
        rounds_strs = rounds_str.split(';')
        return Game(n, list(map(Round.parse, rounds_strs)))

    def is_possible(self):
        return all(round.is_possible() for round in self.rounds)


def load_data():
    with open('data.txt') as f:
        for line in f:
            yield Game.parse(line)


def main():
    res = sum(game.n for game in load_data() if game.is_possible())
    print(res)


if __name__ == '__main__':
    main()
