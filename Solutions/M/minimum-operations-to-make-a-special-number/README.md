# Minimum operations to make a special number

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-a-special-number/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution {
 public:
  int work(const string& s, const string& t) {
    for (int i = 0, j = 0; s[i]; ++i)
      if (s[i] == t[j] and !t[++j]) return i - 1;
    return INT_MAX;
  }
  int minimumOperations(string num) {
    reverse(num.begin(), num.end());
    int ret = num.size() - (num.find("0") != string::npos);
    for (string s : {"00", "05", "52", "57"}) ret = min(ret, work(num, s));
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
