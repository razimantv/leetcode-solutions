# Maximum value after insertion

[Problem link](https://leetcode.com/problems/maximum-value-after-insertion)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-value-after-insertion

class Solution {
 public:
  string maxValue(string n, int x) {
    int N = n.size();
    if (n[0] == '-') {
      for (int i = 1; i < N; ++i) {
        if (n[i] - '0' > x)
          return n.substr(0, i) + ((char)('0' + x)) + n.substr(i);
      }
    } else {
      for (int i = 0; i < N; ++i) {
        if (n[i] - '0' < x)
          return n.substr(0, i) + ((char)('0' + x)) + n.substr(i);
      }
    }
    return n + (char)(x + '0');
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
