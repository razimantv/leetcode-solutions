// https://leetcode.com/problems/word-search-ii

class Solution {
 public:
  inline static vector<vector<int>> dir = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
  unordered_set<string> seen, pref, wordset;
  void dfs(vector<vector<char>>& board, int i, int j, string s, int M, int N) {
    s += board[i][j];
    if (!pref.count(s)) return;
    if (wordset.count(s)) seen.insert(s);
    board[i][j] = '#';
    for (auto d : dir) {
      int ii = i + d[0], jj = j + d[1];
      if (ii >= 0 and ii < M and jj >= 0 and jj < N and board[ii][jj] != '#')
        dfs(board, ii, jj, s, M, N);
    }
    board[i][j] = s.back();
    return;
  }
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    seen.clear();
    pref.clear();
    wordset.clear();

    for (auto w : words) {
      wordset.insert(w);
      string s = "";
      for (auto c : w) {
        s += c;
        pref.insert(s);
      }
    }

    int M = board.size(), N = board[0].size();
    for (int i = 0; i < M; i++)
      for (int j = 0; j < N; j++) dfs(board, i, j, "", M, N);

    vector<string> ret;
    for (auto s : seen) ret.push_back(s);
    return ret;
  }
};
