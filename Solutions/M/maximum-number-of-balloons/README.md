# Maximum number of balloons

[Problem link](https://leetcode.com/problems/maximum-number-of-balloons)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-balloons

class Solution {
 public:
  int maxNumberOfBalloons(string text) {
    vector<int> cnt(26);
    for (char c : text) ++cnt[c - 'a'];

    return min(min(min(cnt[0], cnt[1]), min(cnt[11], cnt[14]) / 2), cnt[13]);
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
