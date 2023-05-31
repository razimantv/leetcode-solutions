# Two sum ii input array is sorted

[Problem link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution {
 public:
  vector<int> twoSum(vector<int>& num, int target) {
    int n = num.size(), i = 0, j = n - 1;
    while (i < j) {
      if (num[i] + num[j] == target)
        return {++i, ++j};
      else if (num[i] + num[j] < target)
        ++i;
      else
        --j;
    }
    return {};
  }
};
```