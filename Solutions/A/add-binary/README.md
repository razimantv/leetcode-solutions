# Add binary

[Problem link](https://leetcode.com/problems/add-binary)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/add-binary

class Solution {
 public:
  string addBinary(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    if (a.size() < b.size()) swap(a, b);
    char carry = 0;
    string ret = "";
    int N = a.size(), M = b.size();
    for (int i = 0; i < N; ++i) {
      char cur = a[i] - '0' + carry;
      if (i < M) cur += b[i] - '0';
      carry = cur > 1;
      ret += '0' + (cur & 1);
    }
    if (carry) ret += '1';
    reverse(ret.begin(), ret.end());
    return ret;
  }
};
```
## Tags

* [Integer operations on strings](/Collections/integer-operations-on-strings.md#integer-operations-on-strings)
