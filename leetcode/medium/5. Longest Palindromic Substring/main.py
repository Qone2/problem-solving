class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l = -1
        max_s = ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            beat_len = max(len1, len2)
            if beat_len[0] > max_l:
                max_l = beat_len[0]
                start = beat_len[1] + 1
                end = beat_len[2] - 1
        max_s = s[start:end + 1]

        return max_s

    def expand_around_center(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left, right


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))
