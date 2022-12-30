from typing import *


def solution(tickets: List[List[str]]) -> List[str]:
    answer = ["ICN"]
    # 방문여부 선언
    visited = list(False for _ in range(len(tickets)))
    dfs("ICN", sorted(tickets, key=lambda x: x[1]), visited, -1, answer)
    return answer


def dfs(current: str, tickets: List[List[str]], visited: List[bool], idx, answer: List[str]):
    # 방문처리
    if idx == -1:
        pass
    else:
        visited[idx] = True
    # 종료조건
    if len(answer) == len(tickets) + 1:
        return
    for i, t in enumerate(tickets):
        if visited[i] is False and t[0] == current:
            answer.append(t[1])
            dfs(t[1], tickets, visited[:], i, answer)
            if len(answer) == len(tickets) + 1:
                return
            answer.pop()


if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"],
                    ["BBB", "AAA"]]))
