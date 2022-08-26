// https://leetcode.com/problems/global-and-local-inversions

class Solution {
 public:
  bool isIdealPermutation(vector<int>& A) {
    int lim = 0;
    for (int i = 0, N = A.size(); i < N; ++i) {
      if (A[i] < lim) return false;
      if (i) lim = max(lim, A[i - 1]);
    }
    return true;
  }
};
