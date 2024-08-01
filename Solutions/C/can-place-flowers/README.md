# Can place flowers

[Problem link](https://leetcode.com/problems/can-place-flowers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/can-place-flowers

class Solution {
 public:
  bool canPlaceFlowers(vector<int>& fb, int n) {
    for (int i = 0, N = fb.size(); n and i < N; ++i) {
      if (!fb[i] and (!i or !fb[i - 1]) and (i == N - 1 or !fb[i + 1]))
        --n, ++fb[i];
    }
    return !n;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
