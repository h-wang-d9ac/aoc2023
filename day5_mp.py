# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:01:55 2023

@author: Hanchen Wang
"""

def map_loc_step(n, mapped):
    for mapping in mapped:
        for step in mapping:
            if n >= step[0] and n < step[1]:
                n += step[2]
                break

    return n


def mp_map_loc(mp_args):
    seed_range = mp_args[0]
    mapped = mp_args[1]
    loc = [map_loc_step(n, mapped) for n in range(seed_range[0], seed_range[1])]
    return min(loc)

def mp_map_loc_full(mp_args):
    seed_range = mp_args[0]
    mapped = mp_args[1]
    loc = [map_loc_step(n, mapped) for n in range(seed_range[0], seed_range[1])]
    return loc
