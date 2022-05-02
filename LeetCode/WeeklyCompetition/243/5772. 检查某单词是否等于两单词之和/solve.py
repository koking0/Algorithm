class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(s: str) -> int:
            return int(''.join([str(ord(c) - ord('a')) for c in s]))

        return convert(firstWord) + convert(secondWord) == convert(targetWord)


if __name__ == '__main__':
    print(Solution().isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa"))
