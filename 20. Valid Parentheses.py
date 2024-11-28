class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        for ele in s:
            if (ele in '({['):
                stack.append(ele)
            else:
                if (len(stack) == 0):
                    return False
                else:
                    cur = stack.pop()
                    if (opening.index(cur) != closing.index(ele)):
                        return False
        return len(stack) == 0
