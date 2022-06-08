class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            returnString = commonPrefix(strs[0], strs[1])
            return returnString
        else:
            strs2 = [strs[x] for x in range(len(strs) // 2)]
            strs3 = [strs[y] for y in range((len(strs) // 2) + 1, len(strs))]
            lcp1 = Solution.longestCommonPrefix(self, strs2)
            lcp2 = Solution.longestCommonPrefix(self, strs3)
            return Solution.commonPrefix(lcp1, lcp2)

    def commonPrefix(str1, str2) -> str:
        k = min(len(str1), len(str2))
        rString = ""
        for x in range(k):
            if str1[x] == str2[x]:
                rString = rString + str1[x]
            else:
                return rString


#A quick test
obj = Solution()
testStrs = ["flower", "flow", "flight"]
print(obj.longestCommonPrefix(testStrs))
testStrs2 = ["dog", "racecar", "car"]
print(obj.longestCommonPrefix(testStrs2))