# Maximum odd binary number

[Problem link](https://leetcode.com/problems/maximum-odd-binary-number/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-odd-binary-number/

class Solution {
 public:
  string maximumOddBinaryNumber(string s) {
    sort(s.begin(), s.end(), greater<char>());
    return s.substr(1) + "1";
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
