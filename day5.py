# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:06:48 2023

@author: Hanchen Wang
"""


def read_input(path):
    seeds = []
    data = {}
    curr_map = ""
    with open(path) as file:
        for line in file:
            if line.isspace():
                continue
            if "seeds:" in line:
                seeds = [
                    int(s) for s in line.strip().split(":")[1].strip().split()
                ]
                continue
            if ":" in line:
                curr_map = line.strip().split()[0]
                map_from, map_to = curr_map.split("-to-")
                data[map_from] = {"to": map_to, "src": {}, "dest": {}}
                continue

            dest, src, length = [int(s) for s in line.strip().split()]
            data[map_from]["src"].update({src: length})
            data[map_from]["dest"].update({src: dest - src})

    return seeds, data


def map_input(path):
    with open(path) as file:
        seeds, *maps = file.read().split("\n\n")

    seeds = [int(s) for s in seeds.split(":")[1].split()]

    mapped = []
    for m in maps:
        _, *mapping = m.strip().split("\n")
        step = []
        for n in mapping:
            dest, src, rng = [int(k) for k in n.split()]
            step.append((src, src + rng, dest - src))
        mapped.append(step)

    return seeds, mapped


def map_loc_step(n, mapped):
    for mapping in mapped:
        for step in mapping:
            if n >= step[0] and n < step[1]:
                n += step[2]
                break

    return n


def map_loc(n, f, data, target="location"):
    dest = n
    for mapped, length in data[f]["src"].items():
        if n >= mapped and n < mapped + length:
            dest = n + data[f]["dest"][mapped]
            break

    if data[f]["to"] != target:
        return map_loc(dest, data[f]["to"], data, target)
    else:
        # print()
        return dest



def part1(path):
    seed, data = read_input(path)
    loc = [map_loc(s, "seed", data) for s in seed]

    return min(loc)


def part2(path):
    seed_list, mapped = map_input(path)
    seeds_range = [(seed_list[i], seed_list[i] + seed_list[i+1]) for i in range(0, len(seed_list), 2)]
    l = [map_loc_step(n, mapped) for n in seed_list]


def invert_map(data):
    data_inv = {}
    for src, val in data.items():
        data_inv[val["to"]] = {"to": src, "src": {}, "dest": {}}
        for s, d in val["dest"].items():
            data_inv[val["to"]]["src"].update({s + d: val["src"][s]})
            data_inv[val["to"]]["dest"].update({s + d: -d})

    return data_inv

