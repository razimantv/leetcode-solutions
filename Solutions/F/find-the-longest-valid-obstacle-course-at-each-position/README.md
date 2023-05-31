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

* [Dynamic programming](/README.md#Dynamic_programming) > [Longest increasing subsequence](/README.md#Dynamic_programming-Longest_increasing_subsequence)
* [Binary search](/README.md#Binary_search)
