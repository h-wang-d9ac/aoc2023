# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:03:31 2023

@author: Hanchen Wang
"""

def read_input(path):

    imgs = [[j.strip() for j in i.strip().split("\n")] for i in open(path).read().strip().split("\n\n")]
    
    return imgs


def rotate_img(img, r, c):
    r_img = []
    for i in range(c):
        r_img.append("".join([img[j][i] for j in range(r)]))
        
    return r_img, c, r


def find_sym(img, r):
    
    sym = -1
    for i in range(r - 1):
        top = img[:i + 1]
        bottom = img[i+1:]
        if all(top[-(j + 1)] == bottom[j] for j in range(min(i + 1, r - i - 1))):
            sym = i + 1
            break
            
    return sym
            

def find_reflect(img, r, c):
    sym = find_sym(img, r)
    if sym == -1:
        r_img, r_r, r_c = rotate_img(img, r, c)
        sym = find_sym(r_img, r_r)
    else:
        sym = sym * 100
    
    return sym


def p1(path):
    imgs = read_input(path)
    reflect = [find_reflect(img, len(img), len(img[0])) for img in imgs]
    
    return sum(reflect)
    

def find_diffs(img, r):
    
    diffs = []
    for i in range(r - 1):
        top = img[:i + 1]
        bottom = img[i+1:]
        comp_len = min(len(top), len(bottom))
        diffs.append(sum(sum(1 for a, b in zip(top[-(j + 1)], bottom[j]) if a != b) for j in range(comp_len)))
            
    return diffs


def find_err(img, r, c):
    r_diff = find_diffs(img, r)
    r_img, r_r, r_c = rotate_img(img, r, c)
    c_diff = find_diffs(r_img, r_r)
    
    return [r_diff, c_diff]


def p2(path):
    imgs = read_input(path)
    diffs = [find_err(img, len(img), len(img[0])) for img in imgs]
    
    diff_num = []
    for diff in diffs:
        d = 1

        if diff[0].count(1) == 1:
            test = diff[0]
            d = 100
        else:
            test = diff[1]
                
        for j in range(len(test)):
            if test[j] == 1:
                d = d * (j + 1)
                break
        
        diff_num.append(d)
    
    return sum(diff_num)