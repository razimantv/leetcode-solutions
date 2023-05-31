# Rotating the box

[Problem link](https://leetcode.com/problems/rotating-the-box)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rotating-the-box

class Solution {
 public:
  vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
    int n = box.size(), m = box[0].size();
    vector<vector<char>> ret(m, vector<char>(n));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) ret[i][j] = box[n - 1 - j][i];

    for (int j = 0; j < n; ++j) {
      for (int i = m - 1; i >= 0;) {
        if (ret[i][j] == '*') {
          --i;
          continue;
        }
        int ii = i, cnt = 0;
        while (ii >= 0 and ret[ii][j] != '*') {
          if (ret[ii--][j] == '#') ++cnt;
        }

        for (int k = 0; k < cnt; ++k) ret[i - k][j] = '#';
        for (i -= cnt; i > ii; --i) ret[i][j] = '.';
      }
    }
    return ret;
  }
};

/*

b00 b0m
bn0 bnm

bn0 b00
bnm b0m
*/
```