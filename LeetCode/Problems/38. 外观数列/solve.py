class Solution:
    def countAndSay(self, n: int) -> str:
        cnt, ans = 0, "1"
        while cnt < n - 1:
            tmp, tmp_str = "", ""
            for i in ans:
                if not tmp_str or i == tmp_str[-1]:
                    tmp_str += i
                else:
                    tmp += f"{len(tmp_str)}{tmp_str[0]}"
                    tmp_str = i
            if tmp_str:
                tmp += f"{len(tmp_str)}{tmp_str[0]}"
            ans = tmp
            cnt += 1
        return ans


if __name__ == '__main__':
    print(Solution().countAndSay(5))
