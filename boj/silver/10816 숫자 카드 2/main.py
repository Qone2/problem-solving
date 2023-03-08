from collections import defaultdict

if __name__ == "__main__":
    input()
    cards = list(map(int, input().split()))
    input()
    card_map = defaultdict(int)
    for card in cards:
        card_map[card] += 1

    tests = list(map(int, input().split()))
    for test in tests:
        print(card_map[test], end=' ')
