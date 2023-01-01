def up_down(char):
    return min(ord('Z') + 1 - ord(char), ord(char) - ord('A'))

def solution(name):
    needs = list(filter(lambda i: name[i] != 'A', range(1, len(name))))
    if not needs:
        left_rights = 0
    else:
        left_rights = min(max(needs), len(name) - min(needs))

    up_downs = sum(list(map(up_down, name)))
    return left_rights + up_downs


if __name__=="__main__":
    print(solution("ABAAAAAAAAABB"))