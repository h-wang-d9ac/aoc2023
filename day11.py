# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:01:00 2023

@author: Hanchen Wang
"""
import itertools

def read_input(path):
    with open(path) as file:
        gal_map = [[l for l in line.strip()] for line in file]
    
    return gal_map, len(gal_map[0]), len(gal_map)


def rotate_map(gal_map, x, y):
    new_map = []
    for i in range(x):
        new_map.append([gal_map[j][i] for j in range(y)])
        
    return new_map, y, x


def add_row(gal_map, x, y, k=1):
    add_y = 0
    exp_y_map = []
    
    for i in range(y):
        exp_y_map.append(gal_map[i])
        if all(s == "." for s in gal_map[i]):
            add_y += k
            exp_y_map.extend([["."] * x] * k)
    
    return exp_y_map, y + add_y


def expand_map(gal_map, x, y, k=1):
    exp_y_map, a_y = add_row(gal_map, x, y, k)    
            
    r_map, r_x, r_y = rotate_map(exp_y_map, x, a_y)
    
    exp_ry_map, a_ry = add_row(r_map, r_x, r_y, k) 
                
    exp_map, e_x, e_y = rotate_map(exp_ry_map, r_x, a_ry)
    
    return exp_map, e_x, e_y

    
def get_coords(gal_map, x, y):
    gal_coords = []
    for i in range(y):
        for j in range(x):
            if gal_map[i][j] == "#":
                gal_coords.append((i, j))
                
    return gal_coords


def get_dist(gal_coords):
    gal_pairs = list(itertools.combinations(gal_coords, 2))
    
    dist = [(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])) for p in gal_pairs]
    
    return dist
    

def p1(path):
    gal_map, x, y = read_input(path)
    e_map, e_x, e_y = expand_map(gal_map, x, y)
    gal_coords = get_coords(e_map, e_x, e_y)
    gal_dist = get_dist(gal_coords)
    
    return sum(gal_dist)


def get_empty(gal_map, x, y):
    y_space = []
    x_space = []
    for i in range(y):
        if all(s == "." for s in gal_map[i]):
            y_space.append(i)

    for j in range(x):
        if all(gal_map[i][j] == "." for i in range(y)):
            x_space.append(j)
    
    return x_space, y_space
    
    
def calc_dist(gal_coords, x_s, y_s, k=1):
    gal_pairs = list(itertools.combinations(gal_coords, 2))
    dist = []
    for pair in gal_pairs:
        x_d = abs(pair[0][0] - pair[1][0])
        x_exp = len(set(range(min(pair[0][0], pair[1][0]) + 1, max(pair[0][0], pair[1][0]))).intersection(set(y_s)))

        y_d = abs(pair[0][1] - pair[1][1])
        y_exp = len(set(range(min(pair[0][1], pair[1][1]) + 1, max(pair[0][1], pair[1][1]))).intersection(set(x_s)))

        dist.append(sum([x_d, x_exp * (k-1), y_d, y_exp * (k-1)]))
        
    return dist
        
    
def p2(path, k):
    gal_map, x, y = read_input(path)
    gal_coords = get_coords(gal_map, x, y)
    x_s, y_s = get_empty(gal_map, x, y)
    
    dist = calc_dist(gal_coords, x_s, y_s, k)
    
    return sum(dist)
        
        
    