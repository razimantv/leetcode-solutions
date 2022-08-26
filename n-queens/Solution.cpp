// https://leetcode.com/problems/n-queens

class Solution {
 public:
  vector<vector<string>> solveNQueens(int n) {
    vector<string> boardbase(n, string(n, '.'));

    vector<vector<string>> ret;
    vector<int> perm(n);
    iota(perm.begin(), perm.end(), 0);
    do {
      int flag = true;
      for (int i = 0; flag and i < n; ++i)
        for (int j = 0; flag and j < i; ++j)
          if (abs(perm[i] - perm[j]) == i - j) flag = false;
      if (flag) {
        vector<string> board = boardbase;
        for (int i = 0; i < n; ++i) board[i][perm[i]] = 'Q';
        ret.push_back(board);
      }
    } while (next_permutation(perm.begin(), perm.end()));
    return ret;
  }
};
