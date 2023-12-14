# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:59:35 2023

@author: Hanchen Wang
"""
import itertools

def read_input(path):

    lines = []
    counts = []

    with open(path) as file:
        for line in file:
            l, c = line.split()
            lines.append(l)
            counts.append([int(i.strip()) for i in c.split(",")])
        
    
    
    return lines, counts


def count_line(line):
    grps = line.split(".")
    counts = [len(g) for g in grps if (g != "." and g != "")]
    
    return counts


def get_unknown(line):
    unknown = [i for i in range(len(line)) if line[i] == "?"]
    
    return unknown



def gen_positions(line, count):
    unknown = get_unknown(line)
    find = sum(count)
    known = line.count("#")
    
    pos_com = list(itertools.combinations(unknown, find - known))
    
    pass_line = []
    for comb in pos_com:
        test_line = [c for c in line.replace("?", ".")]

        for i in comb:
            test_line[i] = "#"
        if count_line("".join(test_line)) == count:
            pass_line.append(comb)
            
    return pass_line


def p1(path):
    lines, counts = read_input(path)
    
    pos_lines = [gen_positions(lines[i], counts[i]) for i in range(len(lines))]
    
    pos_counts = [len(p) for p in pos_lines]
    
    return sum(pos_counts)


def check_line(line, count, pos, grp, seq, checked=None):
    if checked is None:
        checked = {}

    if (pos, grp, seq) in checked:
        return checked[(pos, grp, seq)]
    
    if pos == len(line):
        if grp == len(count):
            if seq == 0:
                return 1
            else:
                return 0
        elif grp == len(count) - 1:
            if seq == count[grp]:
                return 1
            else:
                return 0
        elif grp < len(count) - 1:
            return 0

    valid = 0
    
    if line[pos] == "#":
        if grp < len(count):
            if seq < count[grp]:
                valid += check_line(line, count, pos + 1, grp, seq + 1, checked)
                
    elif line[pos] == ".":
        if seq == 0 or grp >= len(count):
            valid += check_line(line, count, pos + 1, grp, 0, checked)
        elif seq == count[grp]:
            valid += check_line(line, count, pos + 1, grp + 1, 0, checked)
            
    elif line[pos] == "?":
        if seq == 0 or grp >= len(count):
            valid += check_line(line, count, pos + 1, grp, 0, checked)
        elif seq == count[grp]:
            valid += check_line(line, count, pos + 1, grp + 1, 0, checked)

        if grp < len(count):
            if seq < count[grp]:
                valid += check_line(line, count, pos + 1, grp, seq + 1, checked)
        
    checked[(pos, grp, seq)] = valid
    
    return valid


def p2(path):
    lines, counts = read_input(path)
    
    new_lines = ["?".join([line] * 5) for line in lines]
    new_counts = [count * 5 for count in counts]
    
    valid_combos = [check_line(new_lines[i], new_counts[i], 0, 0, 0) for i in range(len(new_lines))]
    
    
    return sum(valid_combos)
