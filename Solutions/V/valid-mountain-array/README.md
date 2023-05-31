# Valid mountain array

[Problem link](https://leetcode.com/problems/valid-mountain-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-mountain-array

class Solution {
 public:
  bool validMountainArray(vector<int>& arr) {
    bool u{0}, d{0};
    for (int i = 1, n = arr.size(); i < n; ++i) {
      if (arr[i] > arr[i - 1]) {
        if (!d)
          u = true;
        else
          return false;
      } else if (arr[i] < arr[i - 1]) {
        if (u)
          d = true;
        else
          return false;
      } else
        return false;
    }
    return u && d;
  }
};
```