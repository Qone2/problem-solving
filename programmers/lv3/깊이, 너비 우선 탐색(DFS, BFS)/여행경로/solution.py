from collections import deque, defaultdict


def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = deque(["ICN"])
    while stack:
        temp = stack[-1]

        if not routes[temp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[temp].pop())
    answer.reverse()

    return answer


if __name__ == "__main__":
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    print(solution([["ICN", "ATL"], ["ICN", "SFO"], ["ATL", "SFO"], ["SFO", "ICN"], ["SFO", "ATL"]]))
    print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"],
                    ["BBB", "AAA"]]))
