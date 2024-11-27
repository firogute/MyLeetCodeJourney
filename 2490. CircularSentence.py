class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        lst = sentence.split()
        if len(lst) == 1:
            return lst[0][0] == lst[0][-1]
        else:
            bool = True
            for i in range(len(lst)-1):
                bool = bool and (lst[i][-1] == lst[i+1][0])
                if (not bool):
                    return bool
            return bool and lst[0][0] == lst[-1][-1]
