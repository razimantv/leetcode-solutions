# Maximum element after decreasing and rearranging

[Problem link](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging

class Solution {
 public:
  int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
    sort(arr.begin(), arr.end());
    for (int i = 0, cur = 1, n = arr.size(); i < n; ++i) {
      arr[i] = min(arr[i], cur);
      cur = arr[i] + 1;
    }
    return arr.back();
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
