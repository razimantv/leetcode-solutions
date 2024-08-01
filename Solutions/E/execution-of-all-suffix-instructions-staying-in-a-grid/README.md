# Execution of all suffix instructions staying in a grid

[Problem link](https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid

class Solution {
 public:
  vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
    int m = s.size(), p1s = startPos[0], p2s = startPos[1];
    vector<int> p1vec(m + 1), p2vec(m + 1);
    for (int i = 0, curp1 = 0, curp2 = 0; i < m; ++i) {
      if (s[i] == 'L')
        --curp2;
      else if (s[i] == 'R')
        ++curp2;
      else if (s[i] == 'U')
        --curp1;
      else
        ++curp1;
      p1vec[i + 1] = curp1;
      p2vec[i + 1] = curp2;
    }

    unordered_map<int, int> p1seen, p2seen;
    vector<int> ret(m);
    for (int i = m - 1; i >= 0; --i) {
      int& cur = ret[i];
      cur = m - i;

      p1seen[p1vec[i + 1]] = i;
      p2seen[p2vec[i + 1]] = i;

      // Problem occurs when we reach a boundary (-1 or n) from this point
      // if j is a problem point, pos(i) + sum of moves from i to j = b
      // => pos[i] + sum (0:j) - sum (0:i-1) = b
      // => b + sum(0:i-1) - pos[i] is seen
      if (p1seen.count(n - p1s + p1vec[i]))
        cur = min(cur, p1seen[n - p1s + p1vec[i]] - i);
      if (p1seen.count(-1 - p1s + p1vec[i]))
        cur = min(cur, p1seen[-1 - p1s + p1vec[i]] - i);
      if (p2seen.count(n - p2s + p2vec[i]))
        cur = min(cur, p2seen[n - p2s + p2vec[i]] - i);
      if (p2seen.count(-1 - p2s + p2vec[i]))
        cur = min(cur, p2seen[-1 - p2s + p2vec[i]] - i);
    }

    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
