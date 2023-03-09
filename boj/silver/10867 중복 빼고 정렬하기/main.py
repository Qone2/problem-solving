if __name__ == "__main__":
    input()
    arr = list(map(int, input().split()))
    num_set = set(arr)
    num_list = list(num_set)
    num_list.sort()
    for l in num_list:
        print(l, end=' ')
