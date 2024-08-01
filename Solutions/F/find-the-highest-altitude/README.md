# Find the highest altitude

[Problem link](https://leetcode.com/problems/find-the-highest-altitude/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
 public:
  int largestAltitude(vector<int>& gain) {
    int ret{}, pref{};
    for (int x : gain) ret = max(ret, pref += x);
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
