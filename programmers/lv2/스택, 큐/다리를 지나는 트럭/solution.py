from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 큐선언
    queue = deque()
    truck_queue = deque(truck_weights)
    # 시간 선언
    time = 0
    # 큐에 길이 - 1 만큼 0삽입
    for _ in range(bridge_length):
        queue.append(0)
    # 무게합 선언
    w_sum = 0
    # 대기가 빌때까지
    while len(truck_queue) > 0 or w_sum > 0:
        # 큐에서 하나뺌
        # 무게 합도 뺌
        w_sum -= queue.popleft()
        # 시간 증가
        time += 1
        if len(truck_queue) == 0:
            continue
        # 무게확인
        if w_sum + truck_queue[0] > weight:
            # 불합이면 0삽입
            queue.append(0)
        else:
            # 합이면 트럭 삽입
            truck = truck_queue.popleft()
            queue.append(truck)
            w_sum += truck

    return time


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
