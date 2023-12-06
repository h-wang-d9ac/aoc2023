# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:49:14 2023

@author: Hanchen Wang
"""

def read_races(path):
    with open(path) as file:
        read_in = file.read().strip().split("\n")
        
    times = [int(n) for n in read_in[0].split(":")[1].strip().split()]
    dists = [int(n) for n in read_in[1].split(":")[1].strip().split()]
    
    return times, dists
    

def solve_quad(dur, rec):
    # dist = (dur - char) * char = dur * char - char ^ 2
    # solve for dist > rec -> dur * char - rec - char ^ 2  > 0
    # find roots
    char_l = (-dur + ((dur ** 2 - (4 * -1 * (-rec)))**(1/2))) / (-2)
    char_h = (-dur - ((dur ** 2 - (4 * -1 * (-rec)))**(1/2))) / (-2)

    lower = int(char_l) + 1
    upper = int(char_h)
    upper = upper - 1 if upper == char_h else upper
    
    return lower, upper

def p1(path):
    times, dists = read_races(path)
    solves = [solve_quad(times[i], dists[i]) for i in range(len(times))]
    
    solve_counts = [solve[1] - solve[0] + 1 for solve in solves]
    
    p = 1
    for i in solve_counts:
        p = p * i
        
    return p


def p2(path):
    times, dists = read_races(path)
    solves = [solve_quad(times[i], dists[i]) for i in range(len(times))]
    
    r_time = int("".join(str(time) for time in times))
    r_dist = int("".join(str(dist) for dist in dists))
    
    solve = solve_quad(r_time, r_dist)                 
    
    return solve[1] - solve[0] + 1
