# Find the array concatenation value

[Problem link](https://leetcode.com/problems/find-the-array-concatenation-value/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution {
 public:
  long long findTheArrayConcVal(vector<int>& nums) {
    int n = nums.size();
    long long ret{};
    for (int i = 0, j = n - 1; i <= j; ++i, --j) {
      if (i == j) {
        ret += nums[i];
        break;
      }
      string s1 = to_string(nums[i]), s2 = to_string(nums[j]);
      ret += stoi(s1 + s2);
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
