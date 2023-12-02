# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:34:19 2023

@author: Hanchen Wang
"""


def check_draw(drawn, bag):
    for c in drawn:
        if drawn[c] > bag[c]:
            return False

    return True


def check_game(game, bag):
    for draw in game:
        if not check_draw(draw, bag):
            return False

    return True


def parse_line(line):
    game = line.split("\n")[0].split(": ")
    game_num = int(game[0].split(" ")[-1])
    sets = []
    for drawn in game[1].split("; "):
        this_set = {}
        for dice in drawn.split(", "):
            pair = dice.split(" ")
            this_set[pair[1]] = int(pair[0])
        sets.append(this_set)

    return {game_num: sets}


def get_games(path):
    games = {}

    with open(path) as f:
        for line in f:
            games.update(parse_line(line))

    return games


def test_game(path):
    games = get_games(path)

    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    possible = []
    for game in games:
        if check_game(games[game], bag):
            possible.append(game)

    return sum(possible)


def min_dice(game):
    curr_min = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for dice_set in game:
        for color in curr_min:
            if color in dice_set:
                curr_min[color] = max(curr_min[color], dice_set[color])

    return curr_min

def game_2(path):
    games = get_games(path)
    game_mins = {}
    game_power = []
    for game in games:
        game_mins[game] = min_dice(games[game])
        curr_power = 1
        for color, color_min in game_mins[game].items():
            curr_power = curr_power * color_min
        game_power.append(curr_power)

    return sum(game_power)


