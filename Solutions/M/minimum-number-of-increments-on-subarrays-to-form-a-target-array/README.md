# Minimum number of increments on subarrays to form a target array

[Problem link](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array

class Solution {
 public:
  int minNumberOperations(vector<int>& target) {
    int cnt = 0, cur = 0;
    for (int n : target) cnt += max(0, n - cur), cur = n;
    return cnt;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
