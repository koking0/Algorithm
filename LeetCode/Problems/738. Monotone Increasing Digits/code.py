class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        index, strN = 1, list(str(N))
        while index < len(strN) and strN[index - 1] <= strN[index]:
            index += 1
        if index < len(strN):
            while index > 0 and strN[index - 1] > strN[index]:
                strN[index - 1] = str(int(strN[index - 1]) - 1)
                index -= 1
            for i in range(index + 1, len(strN)):
                strN[i] = '9'
        return int("".join(strN))
        
    def monotoneIncreasingDigits_violence(self, N: int) -> int:
        for num in range(N, -1, -1):
            if list(str(num)) == sorted(list(str(num))):
                return num


if __name__ == "__main__":
    s = Solution()
    print(s.monotoneIncreasingDigits(332))
