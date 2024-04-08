# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        ret = len(sandwiches)
        for x in sandwiches:
            if cnt[x]:
                cnt[x] -= 1
                ret -= 1
            else:
                break
        return ret
