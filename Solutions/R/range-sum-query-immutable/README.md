# Range sum query immutable

[Problem link](https://leetcode.com/problems/range-sum-query-immutable)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-sum-query-immutable

class NumArray {
 public:
  vector<int> psum;

  NumArray(vector<int>& nums) {
    psum = {0};
    int tot = 0;
    for (int x : nums) psum.push_back(tot += x);
  }

  int sumRange(int left, int right) { return psum[right + 1] - psum[left]; }
};

```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
