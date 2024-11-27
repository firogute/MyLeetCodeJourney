class Solution:
    def compressedString(self, word):
        n = len(word)
        i = 0
        comp = ""

        while i < n:
            cnt = 1
            start = i

            while i + 1 < n and word[start] == word[i + 1]:
                i += 1
                cnt += 1

            while cnt > 0:
                if cnt >= 9:
                    comp += "9" + word[start]
                    cnt -= 9
                else:
                    comp += str(cnt) + word[start]
                    cnt = 0

            i += 1

        return comp
