class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        t = [''] * len(s)
        print(t)
        for i in range(len(s)):
            t[indices[i]] = s[i]
        return ''.join(t)
