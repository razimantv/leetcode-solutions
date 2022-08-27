// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k

class Solution {
 public:
  int work(vector<int>& cum, const vector<int>& ar, int n, int k) {
    set<int> pref{0};
    int ret = INT_MIN;
    for (int i = 0, cur = 0; i < n; ++i) {
      cur += (cum[i] += ar[i]);
      auto sit = pref.lower_bound(cur - k);
      if (sit != pref.end()) ret = max(ret, cur - *sit);
      pref.insert(cur);
    }
    return ret;
  }

  int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
    int m = matrix.size(), n = matrix[0].size(), ret = INT_MIN;
    for (int i = 0; i < m; ++i) {
      vector<int> cum(n);
      for (int j = i; j < m; ++j) ret = max(ret, work(cum, matrix[j], n, k));
    }
    return ret;
  }
};
