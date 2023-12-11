# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:48:43 2023

@author: Hanchen Wang
"""
import math


def read_input(path):
    with open(path) as file:
        data = file.read()

    moves_str, nodes_in = data.split("\n\n")
    moves = moves_str.replace("L", "0").replace("R", "1")

    nodes_lines = [[i.strip() for i in l.strip().split("=")]
                   for l in nodes_in.strip().split("\n")]
    nodes = {n[0]: tuple(n[1][1:-1].split(", ")) for n in nodes_lines}

    return moves, nodes


def p1(path):
    moves, nodes = read_input(path)

    n = 0
    move_n = 0
    move_max = len(moves) - 1

    curr_node = "AAA"

    while curr_node != "ZZZ":
        curr_node = nodes[curr_node][int(moves[move_n])]
        n += 1
        move_n = move_n + 1 if move_n < move_max else 0

    return n


def p2(path):
    moves, nodes = read_input(path)

    move_max = len(moves) - 1

    curr_nodes = [n for n in nodes if n[2] == "A"]
    
    node_moves = []
    
    for curr_node in curr_nodes:
        n = 0
        move_n = 0

        while curr_node[2] != "Z":
            curr_node = nodes[curr_node][int(moves[move_n])]
            n += 1
            move_n = move_n + 1 if move_n < move_max else 0
        node_moves.append(n)


    return node_moves
