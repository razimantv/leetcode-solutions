# To lower case

[Problem link](https://leetcode.com/problems/to-lower-case)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/to-lower-case

class Solution {
 public:
  string toLowerCase(string s) {
    for (char& c : s) c |= ' ';
    return s;
  }
};
```