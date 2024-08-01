# Boats to save people

[Problem link](https://leetcode.com/problems/boats-to-save-people)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/boats-to-save-people

class Solution {
 public:
  int numRescueBoats(vector<int>& people, int limit) {
    int ret = 0;
    sort(people.begin(), people.end());
    for (int i = 0, j = people.size() - 1; i <= j; ++ret, --j) {
      if (people[i] + people[j] <= limit) ++i;
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
