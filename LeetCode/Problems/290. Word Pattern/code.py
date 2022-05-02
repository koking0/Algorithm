class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp = dict()
        for i in range(len(pattern)):
            mapp[pattern[i]] = None
        # print(mapp)

        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        
        for i in range(len(s)):
            if mapp[pattern[i]] is None:
                mapp[pattern[i]] = s[i]
            elif mapp[pattern[i]] != s[i]:
                return False
        return True if len(set(mapp.values())) == len(mapp.values()) else False


if __name__=="__main__":
    s = Solution()
    print(s.wordPattern(pattern="abba", s="dog dog dog dog"))
