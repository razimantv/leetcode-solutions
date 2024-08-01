# Find all good indices

[Problem link](https://leetcode.com/problems/find-all-good-indices/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-all-good-indices/

class Solution {
 public:
  vector<int> goodIndices(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> left(n, 1), right(n, 1), answer;
    for (int i = 1; i < n; ++i)
      if (nums[i] <= nums[i - 1]) left[i] = left[i - 1] + 1;
    for (int i = n - 2; i >= 0; --i)
      if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
    for (int i = k; i < n - k; ++i)
      if (left[i - 1] >= k and right[i + 1] >= k) answer.push_back(i);
    return answer;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
