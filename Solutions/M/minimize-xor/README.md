# Minimize xor

[Problem link](https://leetcode.com/problems/minimize-xor/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-xor/

class Solution {
 public:
  int minimizeXor(int num1, int num2) {
    int cnt = __builtin_popcount(num2), cp = num1;
    unordered_set<int> used;
    for (int i = 30; i >= 0 and cnt; --i) {
      if (cp & (1 << i)) {
        cp ^= (1 << i);
        --cnt;
        used.insert(i);
      }
    }
    for (int i = 0; i <= 30 and cnt; ++i) {
      if (!used.count(i)) {
        cp ^= (1 << i);
        --cnt;
      }
    }
    return num1 ^ cp;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
