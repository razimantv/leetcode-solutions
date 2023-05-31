# Truncate sentence

[Problem link](https://leetcode.com/problems/truncate-sentence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/truncate-sentence

class Solution {
 public:
  string truncateSentence(string s, int k) {
    istringstream ss(s);
    string ret, temp;
    for (int i = 0; i < k; ++i) {
      ss >> temp;
      if (i) ret += " ";
      ret += temp;
    }
    return ret;
  }
};
```