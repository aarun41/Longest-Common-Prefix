class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        returnStr = ""
        k = len(strs[0])
        smallStr = strs[0]
        for x in range(len(strs)):
            if len(strs[x]) < k:
                k = len(strs[x])
                smallStr = strs[x]
        
        for y in range(k):
            for element in strs:
                if element[y] == smallStr[y]:
                    append = True
                else:
                    return returnStr
                
            if append == True:
                returnStr = returnStr + element[y]

#A quick test
obj = Solution()
testStrs = ["flower", "flow", "flight"]
print(obj.longestCommonPrefix(testStrs))
testStrs2 = ["dog", "racecar", "car"]
print(obj.longestCommonPrefix(testStrs2))
