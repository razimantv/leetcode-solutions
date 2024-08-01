# Beautiful array

[Problem link](https://leetcode.com/problems/beautiful-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/beautiful-array

class Solution {
 public:
  vector<int> beautifulArray(int n) {
    if (n == 1) return {1};

    auto ret = beautifulArray((n + 1) >> 1);
    for (int& x : ret) x = ((x << 1) - 1);

    auto add = beautifulArray(n >> 1);
    for (int x : add) ret.push_back(x << 1);

    return ret;
  }
};
```
## Tags

* [Construction](/Collections/construction.md#construction)
