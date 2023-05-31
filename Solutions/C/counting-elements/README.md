# Counting elements

[Problem link](https://leetcode.com/problems/counting-elements)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/counting-elements

class Solution {
 public:
  int countElements(vector<int>& arr) {
    set<int> s;
    for (int n : arr) s.insert(n);
    int ret = 0;
    for (int n : arr)
      if (s.count(n + 1)) ret++;
    return ret;
  }
};
```