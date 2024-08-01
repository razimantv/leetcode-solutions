# Utf 8 validation

[Problem link](https://leetcode.com/problems/utf-8-validation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/utf-8-validation

class Solution {
 public:
  bool validUtf8(const vector<int>& data) {
    for (int pos = 0, n = data.size(); pos < n; ++pos) {
      if (!(data[pos] & 0x80)) continue;
      bool flag = false;
      vector<int> masks{0xc0, 0xe0, 0xf0, 0xf8};
      for (int i = 1; i <= 3; ++i) {
        if ((data[pos] & masks[i]) == masks[i - 1]) {
          if (pos + i >= n) return false;
          for (int j = 0; j < i; ++j)
            if ((data[++pos] & 0xc0) != 0x80) return false;
          flag = true;
        }
      }
      if (!flag) return false;
    }
    return true;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
