# Duplicate zeros

[Problem link](https://leetcode.com/problems/duplicate-zeros)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/duplicate-zeros

class Solution {
 public:
  void duplicateZeros(vector<int>& arr) {
    for (int i = 0, N = arr.size(); i < N; ++i)
      if (arr[i] == 0) arr.insert(arr.begin() + i++, 0), arr.pop_back();
  }
};
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
* [Array scanning](/README.md#Array_scanning) > [In-place modification](/README.md#Array_scanning-In_place_modification)
