# Find the smallest divisor given a threshold

[Problem link](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold

class Solution {
 public:
  int smallestDivisor(vector<int>& nums, int threshold) {
    int start = 0, end = 1e7;
    while (end - start > 1) {
      int tot = 0, mid = (start + end) >> 1;
      for (int n : nums) {
        tot += n / mid + (n % mid > 0);
        if (tot > threshold) break;
      }
      (tot <= threshold ? end : start) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
