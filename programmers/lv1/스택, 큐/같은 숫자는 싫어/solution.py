def solution(arr: list):
    # 리턴배열을 만든다
    answer = []
    # 이전 값을 저장하는 변수 선언
    past = -1
    # arr길이만큼 for문
    for i in range(len(arr)):
        # 이전값과 다르면 리턴배열에 삽입
        if arr[i] != past:
            answer.append(arr[i])
        # 이전값 업데이트
        past = arr[i]

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))
