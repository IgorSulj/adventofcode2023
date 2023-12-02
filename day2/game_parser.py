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

    def power(self):
        return self.red * self.green * self.blue


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

    def min_cubes_for_game(self):
        return Round(
            max(round.blue for round in self.rounds),
            max(round.green for round in self.rounds),
            max(round.red for round in self.rounds),
        )


def load_games():
    with open('data.txt') as f:
        for line in f:
            yield Game.parse(line)
