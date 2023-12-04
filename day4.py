# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:05:33 2023

@author: Hanchen Wang
"""
def win_nums(win, num):
    win_nums = [n for n in num if n in win]

    return win_nums


def parse_line(line):
    card_label, card_nums = line.split(":")
    card_number = card_label.split(" ")[-1]
    win, nums = card_nums.split("|")
    win = [int(n.strip()) for n in win.strip().split(" ") if n != ""]
    nums = [int(n.strip()) for n in nums.strip().split(" ") if n != ""]

    return {
        int(card_number.strip()): {
            "win": win,
            "nums": nums
            }
    }


def read_cards(path):
    cards = {}
    with open(path) as file:
        for line in file:
            cards.update(parse_line(line.strip()))

    return cards

def check_win(cards):
    winning = {}
    for card in cards:
        winning[card] = win_nums(cards[card]["win"], cards[card]["nums"])

    return winning


def win_score(path):
    cards = read_cards(path)
    winning = check_win(cards)
    score = [2 ** (len(win) - 1) for win in winning.values() if len(win) > 0]

    return sum(score)


def win_counts(winning):
    win_count = {card: len(win) for card, win in winning.items()}
    return win_count


def card_stack(win_count):
    card_count = {card: 1 for card in win_count}
    for card in win_count:
        card_count.update(
            {
                win_card: card_count[win_card] + card_count[card]
                for win_card
                in range(card + 1, card + win_count[card] + 1)
            }
        )

    return card_count


def win_cards(path):
    cards = read_cards(path)
    winning = check_win(cards)
    win_count = win_counts(winning)

    card_count = card_stack(win_count)

    return sum(card_count.values())
