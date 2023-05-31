# Reordered power of 2

[Problem link](https://leetcode.com/problems/reordered-power-of-2)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reordered-power-of-2

class Solution {
 public:
  bool reorderedPowerOf2(int N) {
    std::string s = std::to_string(N);
    sort(s.begin(), s.end());
    for (int i = 1; i < 1'000'000'000; i *= 2) {
      std::string ss = std::to_string(i);
      sort(ss.begin(), ss.end());
      if (s == ss) return true;
    }
    return false;
  }
};
```