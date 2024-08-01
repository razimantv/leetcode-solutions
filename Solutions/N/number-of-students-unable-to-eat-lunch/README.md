# Number of students unable to eat lunch

[Problem link](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)

## Solutions


### Solution.py
```py
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
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
