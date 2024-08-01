# Check if there is a valid partition for the array

[Problem link](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array

class Solution {
 public:
  bool validPartition(vector<int>& nums) {
    int n = nums.size();
    vector<bool> good(n + 1);
    good[0] = true;
    if (nums[0] == nums[1]) good[2] = true;
    for (int i = 2; i < n; ++i) {
      if (nums[i] == nums[i - 1] and
          ((nums[i] == nums[i - 2] and good[i - 2]) or good[i - 1]))
        good[i + 1] = true;
      else if (nums[i] == nums[i - 1] + 1 and nums[i] == nums[i - 2] + 2 and
               good[i - 2])
        good[i + 1] = true;
    }
    return good.back();
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
