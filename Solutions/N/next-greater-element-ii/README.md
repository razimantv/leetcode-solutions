# Next greater element ii

[Problem link](https://leetcode.com/problems/next-greater-element-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/next-greater-element-ii

class Solution {
 public:
  vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> stk, ret(n, -1);

    for (int pass = 1; pass <= 2; ++pass) {
      for (int i = 0; i < n; ++i) {
        while (!stk.empty() and nums[stk.back()] < nums[i]) {
          ret[stk.back()] = nums[i];
          stk.pop_back();
        }
        if (pass == 1) stk.push_back(i);
      }
    }
    return ret;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
