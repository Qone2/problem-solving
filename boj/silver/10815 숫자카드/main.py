import sys
from typing import *

# input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    card_list: List[int] = list(map(int, input().split(" ")))
    card_map = dict()
    for card in card_list:
        card_map[card] = True
    M = int(input())
    test_list = list(map(int, input().split(' ')))
    for test in test_list:
        print(1 if test in card_map else 0, end=' ')
