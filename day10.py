# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:03:34 2023

@author: Hanchen Wang
"""

PIPES = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    "S": [],
    ".": [],
}


def read_input(path):
    with open(path) as file:
        tiles_str = [[l.strip() for l in line.strip()] for line in file]
    
    max_y = len(tiles_str)
    max_x = len(tiles_str[0])
    tiles = []
    s = None
    for i in range(max_y):
        tiles.append([])
        for j in range(max_x):
            tiles[i].append(PIPES[tiles_str[i][j]])
            if tiles_str[i][j] == "S":
                s = (i, j)
    
    return tiles, s, max_x, max_y, tiles_str


def find_connect(tiles, max_x, max_y, loc, prev):
    
    if prev == loc:    
        for i in [(1, 0), (0, 1)]:
            inc = (-i[0], -i[1])
            if (loc[0] + i[0]) >= 0 and (loc[1] + i[1]) >= 0 and (loc[0] + i[0]) < max_y and (loc[1] + i[1]) < max_x:
                if inc in tiles[loc[0] + i[0]][loc[1] + i[1]]:
                    if prev is None:
                        connect = (loc[0] + i[0], loc[1] + i[1])
                        break
                    else:
                        if (loc[0] + i[0], loc[1] + i[1]) != prev:
                            connect = (loc[0] + i[0], loc[1] + i[1])
                            break
    
    else:
        ref = (loc[0] + tiles[loc[0]][loc[1]][0][0], loc[1] + tiles[loc[0]][loc[1]][0][1])
        step = tiles[loc[0]][loc[1]][1] if prev == ref else tiles[loc[0]][loc[1]][0]
        connect = (loc[0] + step[0], loc[1] + step[1])
        
    return connect


def loop_steps(path):
    tiles, s, max_x, max_y, tiles_Str = read_input(path)
    
    prev = s
    curr = find_connect(tiles, max_x, max_y, s, s)
    loop = [s]
    while curr != s:
        loop.append(curr)
        connect = find_connect(tiles, max_x, max_y, curr, prev)
        prev = curr
        curr = connect
        
    return loop
    
    
def p1(path):
    loop = loop_steps(path)
    steps = len(loop)

    return int(steps / 2) + steps % 2


def area(loop):
    shoelace_loop = loop + [loop[0]]
    steps = len(shoelace_loop)
    step_sum = []
    
    for i in range(steps - 1):
        step_sum.append(shoelace_loop[i][0] * shoelace_loop[i + 1][1] - shoelace_loop[i][1] * shoelace_loop[i + 1][0])
    
    return sum(step_sum) / 2


def interior(loop):
    loop_area = area(loop)
    loop_interior = loop_area - (len(loop) / 2) + 1
    
    return loop_interior
