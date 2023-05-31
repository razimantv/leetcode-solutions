# Find the difference

[Problem link](https://leetcode.com/problems/find-the-difference)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-difference

class Solution {
 public:
  char findTheDifference(string s, string t) {
    int ans{0};
    for (char c : s) ans ^= c;
    for (char c : t) ans ^= c;
    return ans;
  }
};
```
## Tags

* [Unique/duplicate element finding with bizarro algorithms](/README.md#Unique_duplicate_element_finding_with_bizarro_algorithms)
