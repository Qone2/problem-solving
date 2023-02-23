from collections import deque


class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        queue = deque()
        for c in s:
            queue.append(c)
        while queue:
            c1 = queue.popleft()
            if c1 == 'I':
                if queue:
                    if queue[0] == 'V' or queue[0] == 'X':
                        answer += self.evl(queue.popleft()) - self.evl(c1)
                    else:
                        answer += self.evl(c1)
                else:
                    answer += self.evl(c1)
            elif c1 == 'X':
                if queue:
                    if queue[0] == 'L' or queue[0] == 'C':
                        answer += self.evl(queue.popleft()) - self.evl(c1)
                    else:
                        answer += self.evl(c1)
                else:
                    answer += self.evl(c1)
            elif c1 == 'C':
                if queue:
                    if queue[0] == 'D' or queue[0] == 'M':
                        answer += self.evl(queue.popleft()) - self.evl(c1)
                    else:
                        answer += self.evl(c1)
                else:
                    answer += self.evl(c1)
            else:
                answer += self.evl(c1)

        return answer

    def evl(self, c: str) -> int:
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
