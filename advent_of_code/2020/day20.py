from typing import Any, Dict, List, Tuple
from collections import defaultdict


def take_input(filepath):
    tiles = {}
    with open(filepath, 'r') as f:
        all = f.read()
        tiles_raw = all.split('\n\n')
        for tile_raw in tiles_raw:
            title = int(tile_raw.split(':\n')[0][5:])
            tile_area = tile_raw.split(':\n')[1]
            tile = [list(line) for line in tile_area.split('\n')]
            tiles[title] = tile
    return tiles


def puzzle1(filepath):
    tiles = take_input(filepath)
    # print(tiles[3079])
    for t, tile in tiles.items():
        print(f'\nTile {t}:')
        print_tile(tile)


def print_tile(tile):
    for row in tile:
        print(''.join(row))


def check_tile_match(tile1, tile2):
    # short sides
    # top - top



filepath = '/Users/hkoklu/personal/advent_of_code/2020/day20_test.txt'
# print(puzzle1(filepath))
puzzle1(filepath)