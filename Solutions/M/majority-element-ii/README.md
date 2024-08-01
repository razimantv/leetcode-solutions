# Majority element ii

[Problem link](https://leetcode.com/problems/majority-element-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/majority-element-ii

class Solution {
 public:
  vector<int> majorityElement(vector<int>& nums) {
    int i1 = 0, c1 = 0, i2 = 0, c2 = 0;
    for (int n : nums) {
      if (c1 == 0 or i1 == n)
        i1 = n, ++c1;
      else if (c2 == 0 or i2 == n)
        i2 = n, ++c2;
      else {
        --c2;
        if (--c1 == 0) swap(c1, c2), swap(i1, i2);
      }
    }

    vector<int> ret;
    if (c1) {
      c1 = 0;
      for (int n : nums)
        if (n == i1) ++c1;
      if (3 * c1 > nums.size()) ret.push_back(i1);
    }
    if (c2) {
      c2 = 0;
      for (int n : nums)
        if (n == i2) ++c2;
      if (3 * c2 > nums.size()) ret.push_back(i2);
    }
    return ret;
  }
};
```
## Tags

* [Majority element](/Collections/majority-element.md#majority-element)
