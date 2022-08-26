// https://leetcode.com/problems/candy

class Solution {
 public:
  int candy(vector<int>& ratings) {
    int N = ratings.size();
    vector<int> ret(N, 1);
    for (int i = 1; i < N; ++i)
      if (ratings[i] > ratings[i - 1]) ret[i] = ret[i - 1] + 1;
    for (int i = N - 2; i >= 0; --i)
      if (ratings[i] > ratings[i + 1]) ret[i] = max(ret[i], ret[i + 1] + 1);
    return accumulate(ret.begin(), ret.end(), 0);
  }
};
