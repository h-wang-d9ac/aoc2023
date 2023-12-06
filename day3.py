# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:20:08 2023

@author: Hanchen Wang
"""

def symbol_board(new_line, prev_line=0):
    new_num = sum(
            1 << (i - 1) for i in range(1, len(new_line) + 1)
            if (not new_line[-i].isnumeric()
                and new_line[-i] != "."
                )
        )


    prev_line = 0b0 if prev_line == 0 else prev_line << (len(new_line))

    return prev_line + new_num


def gear_board(new_line, prev_line=0):
    new_num = sum(
            1 << (i - 1) for i in range(1, len(new_line) + 1)
            if new_line[-i] == "*"
        )


    prev_line = 0b0 if prev_line == 0 else prev_line << (len(new_line))

    return prev_line + new_num


def number_board(new_line, prev_line=0):
    new_num = sum(
            1 << (i - 1) for i in range(1, len(new_line) + 1)
            if new_line[-i].isnumeric()
        )


    prev_line = 0b0 if prev_line == 0 else prev_line << (len(new_line))

    return prev_line + new_num


def print_board(board, line_len, lines):
    bstr = f"{board:0>{line_len * lines}b}"

    for i in range(lines):
        for j in range(line_len):
            print(bstr[(i * line_len) + j], end="")
        print("")


def left_zero(line_len, lines):
    line = "0" + ("1" * (line_len - 1))
    board = line * lines
    return int(board, 2)


def right_zero(line_len, lines):
    line = ("1" * (line_len - 1)) + "0"
    board = line * lines
    return int(board, 2)


def symbol_grid(sym_board, l_zero, r_zero, line_len):
    l = (sym_board << 1) & r_zero
    r = (sym_board >> 1) & l_zero
    u = (sym_board << line_len)
    d = (sym_board >> line_len)
    ul = (sym_board << (line_len + 1)) & r_zero
    ur = (sym_board << (line_len - 1)) & l_zero
    dl = (sym_board >> (line_len - 1)) & r_zero
    dr = (sym_board >> (line_len + 1)) & l_zero

    sym_grid = sym_board | l | r | u | d | ul | ur | dl | dr

    return sym_grid


def linked_nums(sym_grid, num_board, l_zero, r_zero, line_len):
    connected = sym_grid & num_board
    connected_l = connected
    connected_r = connected
    for _ in range(line_len):
        connected_l = connected_l | ((connected_l << 1 & r_zero) & num_board)
        connected_r = connected_r | ((connected_r >> 1 & l_zero) & num_board)

    return connected_l | connected_r


def read_input(path, gears=False):
    sym_board = 0
    num_board = 0
    lines = 0
    str_seq = ""
    with open(path) as file:
        for line in file:
            line = line.rstrip()
            str_seq += line
            sym_board = symbol_board(line, sym_board) if not gears else gear_board(line, sym_board)
            num_board = number_board(line, num_board)
            lines += 1

    return sym_board, num_board, len(line), lines, str_seq


def mask_numbers(path):
    sym_board, num_board, line_len, lines, str_seq = read_input(path)
    l_zero = left_zero(line_len, lines)
    r_zero = right_zero(line_len, lines)
    sym_grid = symbol_grid(sym_board, l_zero, r_zero, line_len)
    link_mask = linked_nums(sym_grid, num_board, l_zero, r_zero, line_len)

    str_mask = f"{link_mask:0>{line_len * lines}b}"

    masked_nums = []
    for i in range(len(str_mask)):
        next_char = str_seq[i] if str_mask[i] == "1" else " "
        masked_nums.append(next_char)

    return "".join(masked_nums)


def get_sum(path):
    find_nums = [int(s.strip()) for s in mask_numbers(path).strip().split(" ")]
    return sum(find_nums)


def masked_gears(path):
    sym_board, num_board, line_len, lines, str_seq = read_input(path, gears=True)
    l_zero = left_zero(line_len, 3)
    r_zero = right_zero(line_len, 3)
    num_mask = int("1" * (line_len * 3), 2)

    gear_nums = []
    for i in range(sym_board.bit_length()):
        if sym_board >> i & 1:
            line_num = max(int((i) / line_len), 1)

            this_gear = 1 << (i - (line_len * (line_num - 1)))
            sym_grid = symbol_grid(this_gear, l_zero, r_zero, line_len)
            short_nums = (num_board >> (line_len * (line_num - 1))) & num_mask
            link_mask = linked_nums(sym_grid, short_nums, l_zero, r_zero, line_len)

            short_str = (str_seq + " ")[-((line_num + 2) * line_len + 1):-((line_num - 1) * line_len + 1)]

            masked_str = [short_str[-(j + 1)] if (link_mask >> j & 1) else " " for j in range(link_mask.bit_length())][-1::-1]

            numbers = "".join(masked_str)

            find_nums = [int(s.strip()) for s in numbers.strip().split()]
            if len(find_nums) == 2:
                gear_nums.append(find_nums[0] * find_nums[1])

    return sum(gear_nums)
