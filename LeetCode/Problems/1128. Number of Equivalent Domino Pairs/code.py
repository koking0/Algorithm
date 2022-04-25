class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = dict()
        for d1, d2 in dominoes:
            index = tuple(sorted((d1, d2)))
            if index in d:
                d[index] += 1
            else:
                d[index] = 1
        for i in d:
            ans += d[i] * (d[i] - 1) // 2
        return ans


if __name__ == "__main__":
    solution = Solution()
    solution.numEquivDominoPairs(dominoes=[[1,2],[2,1],[3,4],[5,6]])
