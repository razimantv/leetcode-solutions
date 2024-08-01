# Sort an array

[Problem link](https://leetcode.com/problems/sort-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-an-array/

class Solution {
 public:
  vector<int> sortArray(vector<int>& nums) {
    int n = nums.size();
    for (int i = 1; i < n; ++i) {
      for (int j = i, jp = (j - 1) >> 1; j; j = jp, jp = (j - 1) >> 1)
        if (nums[j] > nums[jp])
          swap(nums[j], nums[jp]);
        else
          break;
    }

    for (int i = 0; i < n - 1;) {
      swap(nums[0], nums[--n]);
      for (int j = 0, c1 = (j << 1) | 1; c1 < n; j = c1, c1 = (j << 1) | 1) {
        int c2 = c1 + 1;
        if (c2 < n and nums[c2] > nums[c1]) c1 = c2;
        if (nums[c1] > nums[j])
          swap(nums[j], nums[c1]);
        else
          break;
      }
    }
    return nums;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Implementation](/Collections/sorting.md#implementation)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
