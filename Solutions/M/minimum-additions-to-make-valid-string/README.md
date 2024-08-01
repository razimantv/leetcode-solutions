# Minimum additions to make valid string

[Problem link](https://leetcode.com/problems/minimum-additions-to-make-valid-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution {
 public:
  int addMinimum(string word) {
    vector<int> dp{1, 2, 0};
    for (char c : word) {
      c -= 'a';
      vector<int> cur(3, 100);
      for (int i = 0; i < 3; ++i) {
        for (int j = (i + 1) % 3, marked = 0, add = 0; marked < 3;
             j = (j + 1) % 3, ++add) {
          if (marked or j == c) {
            ++marked;
            cur[j] = min(cur[j], dp[i] + add);
          }
        }
      }
      dp = cur;
    }
    return dp[2];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
