# Find the longest valid obstacle course at each position

[Problem link](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution {
 public:
  vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
    vector<int> ret, lis;
    for (int x : obstacles) {
      int len = upper_bound(lis.begin(), lis.end(), x) - lis.begin();
      if (len == lis.size())
        lis.push_back(x);
      else
        lis[len] = x;
      ret.push_back(len + 1);
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest increasing subsequence](/Collections/dynamic-programming.md#longest-increasing-subsequence)
* [Binary search](/Collections/binary-search.md#binary-search)
