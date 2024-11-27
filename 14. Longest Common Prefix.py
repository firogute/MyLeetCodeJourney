class Solution:
    def longestCommonPrefix(self, lst: List[str]) -> str:
        com = ""
        for i in range(len(lst[0])):
            for s in lst:
                if i == len(s) or s[i] != lst[0][i]:
                    return com
            com += lst[0][i]

        return com
