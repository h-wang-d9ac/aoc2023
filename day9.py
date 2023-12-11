# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:22:11 2023

@author: Hanchen Wang
"""

def read_input(path):
    with open(path) as file:
        data_series = [[int(n) for n in l.strip().split()][-1::-1] for l in file]
    return data_series
        
def poly_diff(diffs, order):
    for i in range(order - 1):
        diffs[i + 1].append(diffs[i][order - i] - diffs[i][order - i + 1])

    
    diffs.append([diffs[order - 1][j] - diffs[order - 1][j + 1] for j in range(2)])
    return diffs


def get_diffs(series):
    order = 1
    diffs = poly_diff([series], order)

    while any(i != diffs[-2][0] for i in (diffs[-2])):
        order += 1
        diffs = poly_diff(diffs, order)
    
    return diffs


def get_next_diff(series):
    diff = [(series[i] - series[i + 1]) for i in range(len(series) - 1)]
    return diff

def get_all_diffs(series):
    diffs = [series]
    
    while any(d != 0 for d in diffs[-1]):
        diffs.append(get_next_diff(diffs[-1]))
        
    return diffs

def get_next_poly(diffs):
    next_poly = [0]
    for i in range(len(diffs)):
        next_poly.append(next_poly[i] + diffs[-i][0])
        
    return next_poly[-1]

def p1(path):
    data_series = read_input(path)
    next_poly = [get_next_poly(get_all_diffs(series)) for series in data_series]    
    return next_poly


def p2(path):
    data_series = read_input(path)
    next_poly = [get_next_poly(get_all_diffs(series[-1::-1])) for series in data_series]    
    return next_poly