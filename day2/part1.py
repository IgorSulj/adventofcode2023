from game_parser import load_games


def main():
    res = sum(game.n for game in load_games() if game.is_possible())
    print(res)


if __name__ == '__main__':
    main()
