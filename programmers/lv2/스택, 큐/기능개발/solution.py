def solution(progresses: list, speeds: list):
    answer = []
    # while progresses가 빌때까지
    while len(progresses) > 0:
        # 1타임마다 progresses에 speeds만큼 추가
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        # 젤 앞에거가 100이상이면 100 이상인것이 있을때마다 pop left
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            # pop할때마다 count값 증가
            count += 1

        # result list에 count추가
        if count > 0:
            answer.append(count)

    # progresses가 비면 answer리턴
    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
