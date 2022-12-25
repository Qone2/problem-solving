from collections import defaultdict


def solution(k, tangerine):
    """
    딕셔너리에 넣고 개수가 많은 순으로 answer + 1
    """
    answer = 0
    # 딕셔너리 선언
    mandarin = defaultdict(int)
    # 귤들 순회 딕셔너리에 넣기
    for t in tangerine:
        mandarin[t] += 1
    # 딕셔너리 값으로 정렬
    mandarin_list = sorted(mandarin.items(), key=lambda x: x[1], reverse=True)
    # 제일 큰 순서로 k 될때까지 answer
    for m in mandarin_list:
        k -= m[1]
        answer += 1
        if k <= 0:
            return answer

    return len(mandarin_list)


if __name__ == "__main__":
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
