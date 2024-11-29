class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        num = len(students)

        count = Counter(students)

        for i in sandwiches:
            if count[i] > 0:
               num -= 1
               count[i] -= 1
            else:
                return num
        return num
