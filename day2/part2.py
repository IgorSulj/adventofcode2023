from game_parser import load_games


def main():
    res = sum(
        game.min_cubes_for_game().power()
        for game in load_games())
    print(res)


if __name__ == '__main__':
    main()
