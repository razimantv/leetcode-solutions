# The k weakest rows in a matrix

[Problem link](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

class Solution {
 public:
  vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    int N = mat.size();

    vector<pair<int, int>> rows;
    for (int i = 0; i < N; ++i) {
      rows.push_back(
          {lower_bound(mat[i].begin(), mat[i].end(), 0, greater<int>()) -
               mat[i].begin(),
           i});
    }
    sort(rows.begin(), rows.end());

    vector<int> ret;
    for (int i = 0; i < k; ++i) ret.push_back(rows[i].second);
    return ret;
  }
};
```