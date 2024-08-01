# Find the duplicate number

[Problem link](https://leetcode.com/problems/find-the-duplicate-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-duplicate-number

class Solution {
 public:
  int findDuplicate(vector<int>& nums) {
    int n = nums.size();
    int start = 0, end = n - 1;
    while (end - start > 1) {
      int mid = (end + start) >> 1, cnt = 0;
      for (int a : nums)
        if (a <= mid) cnt++;
      if (cnt > mid)
        end = mid;
      else
        start = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
