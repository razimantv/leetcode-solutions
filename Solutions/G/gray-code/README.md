# Gray code

[Problem link](https://leetcode.com/problems/gray-code)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/gray-code

class Solution {
 public:
  vector<int> grayCode(int n) {
    int M = 1 << n;
    vector<int> ret(M);
    for (int i = 0; i < M; ++i) ret[i] = i ^ (i >> 1);
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
