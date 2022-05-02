class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


if __name__ == '__main__':
    s = Solution()
    print(s.isLongPressedName(name="alex", typed="aaleex"))
    print(s.isLongPressedName(name="saeed", typed="ssaaedd"))
    print(s.isLongPressedName(name="leelee", typed="lleeelee"))
    print(s.isLongPressedName(name="laiden", typed="laiden"))
