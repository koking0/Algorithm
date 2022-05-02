class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right, n = 0, len(s1), len(s2)
        while right < n + 1:
            tmp = s2[left:right]
            ss1 = sorted(list(s1))
            ss2 = sorted(list(tmp))
            if ss1 == ss2:
                return True
            left += 1
            right += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("adc", "dcda"))
