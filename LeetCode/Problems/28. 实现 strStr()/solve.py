class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNextArray(arr):
            if len(arr) == 1:
                return [-1]

            next_array = [0 for _ in range(len(arr))]
            next_array[0] = -1
            idx, cn = 2, 0
            while idx < len(arr):
                if arr[idx - 1] == arr[cn]:
                    next_array[idx] = cn + 1
                    idx += 1
                    cn += 1
                elif cn > 0:
                    cn = next_array[cn]
                else:
                    next_array[idx] = 0
                    idx += 1
            return next_array

        def KMP(pattern, target):
            if not target:
                return 0
            if not pattern or not target or len(pattern) < len(target):
                return -1

            pattern, target = list(pattern), list(target)
            idx1, idx2 = 0, 0
            next_array = getNextArray(target)
            while idx1 < len(pattern) and idx2 < len(target):
                if pattern[idx1] == target[idx2]:
                    idx1 += 1
                    idx2 += 1
                elif next_array[idx2] == -1:
                    idx1 += 1
                else:
                    idx2 = next_array[idx2]
            return idx1 - idx2 if idx2 == len(target) else -1

        return KMP(haystack, needle)
