participant = []
completion = []

d = {}


def solution(participant, completion):
    for p in participant:
        if p in d:
            d[p] = d[p] + 1
        else:
            d[p] = 1
    for c in completion:
        if c in d:
            d[c] = d[c] - 1
    for k in d:
        if d[k] == 1:
            return k



#해쉬(딕셔너리)를 사용해야 한다. 밑에 코드를 쓰면 효율성 테스트를 통과하지 못한다.

# def solution(participant, completion):
#     for c in completion:
#         participant.remove(c)
#     return participant[0]
        