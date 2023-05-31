# Length of last word

[Problem link](https://leetcode.com/problems/length-of-last-word)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/length-of-last-word

class Solution {
 public:
  int lengthOfLastWord(string s) {
    istringstream iss(s);
    string a;
    while (iss >> a)
      ;
    return a.size();
  }
};
```
## Tags

* [String](/README.md#String) > [Parsing](/README.md#String-Parsing)
