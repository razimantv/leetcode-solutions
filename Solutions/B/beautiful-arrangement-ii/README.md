# Beautiful arrangement ii

[Problem link](https://leetcode.com/problems/beautiful-arrangement-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/beautiful-arrangement-ii

class Solution {
 public:
  vector<int> constructArray(int n, int k) {
    int start = 1, end = n, cur = 1;
    vector<int> ret;
    while (1) {
      if (k == 1) {
        if (cur)
          for (int i = start; i <= end; ++i) ret.push_back(i);
        else
          for (int i = end; i >= start; --i) ret.push_back(i);
        break;
      } else
        ret.push_back(cur ? (start++) : (end--));
      cur ^= 1;
      --k;
    }
    return ret;
  }
};
```
## Tags

* [Construction](/Collections/construction.md#construction)
