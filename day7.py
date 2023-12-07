# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:24:32 2023

@author: Hanchen Wang
"""
FACE_CARDS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}



class Card:
    def __init__(self, label, joker=False):
        self.label = label
        self.value = FACE_CARDS[label] if label in FACE_CARDS else int(label)
        if joker and self.label == "J":
            self.value = 1
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return self.label


class Hand():
    def __init__(self, cards, bid, joker=False):
        self.bid = bid

        self.cards = [Card(c, joker) for c in cards]
        non_joker = [c for c in self.cards if c.value > 1]
        jokers = 5 - len(non_joker)
        
        self.type = 7 if jokers == 5 else 1
        set_len = len(set(non_joker))
        if set_len == 1:
            self.type = 7
        elif set_len == 2:
            if non_joker.count(non_joker[0]) in [1, (4 - jokers)]:
                self.type = 6
            else:
                self.type = 5
        elif set_len == 3:
            if max([non_joker.count(njc) for njc in non_joker]) == (3 - jokers):
                self.type = 4
            else:
                self.type = 3
        elif set_len == 4:
            self.type = 2


    def __gt__(self, other):
        if self.type == other.type:
            for i in range(5):
                if self.cards[i] == other.cards[i]:
                    continue
                return self.cards[i] > other.cards[i]
            
        return self.type > other.type

    def __repr__(self):
        return "".join([repr(card) for card in self.cards])


def read_input(path, joker=False):
    hands = []
    with open(path) as file:
        for line in file:
            hand, bid = line.strip().split()
            hands.append(Hand(hand, int(bid), joker))
    
    return hands


def p1(path):
    hands = read_input(path)
    hands.sort()
    hand_value = [(hands[i].bid * (i + 1)) for i in range(len(hands))]
    
    return sum(hand_value)


def p2(path):
    hands_j = read_input(path, True)
    hands_j.sort()
    hand_value = [(hands_j[i].bid * (i + 1)) for i in range(len(hands_j))]
    
    return sum(hand_value)
