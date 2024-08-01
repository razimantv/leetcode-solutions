# Minimum operations to make the array increasing

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

class Solution {
 public:
  int minOperations(vector<int>& nums) {
    int cnt = 0, low = 0;
    for (int n : nums) {
      if (n <= low) cnt += low + 1 - n;
      low = max(low + 1, n);
    }
    return cnt;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
