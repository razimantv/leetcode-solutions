// https://leetcode.com/problems/word-search-ii/

struct node {
  unordered_map<char, pair<node*, int>> children;
};

const vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

class Solution {
  node trie;
  int m, n;
  void add(node* n, const string& s, int i) {
    if (!s[i]) {
      n->children['$'] = {nullptr, 1};
      return;
    }

    if (!n->children.count(s[i])) n->children[s[i]] = {new node, 0};
    ++n->children[s[i]].second;
    add(n->children[s[i]].first, s, i + 1);
  }

  int work(vector<vector<char>>& board, int i, int j, node* tn, string& s,
           vector<string>& ret) {
    char c = board[i][j];
    if (!tn->children.count(c)) return 0;

    s += c;
    board[i][j] = '#';
    auto& [next, val] = tn->children[c];

    int sub = 0;
    if (next->children.count('$')) {
      next->children.erase('$');
      ret.push_back(s);
      ++sub;
    }

    for (auto [di, dj] : neigh) {
      int ii = i + di, jj = j + dj;
      if (ii < 0 or ii >= m or jj < 0 or jj >= n) continue;
      int cur = work(board, ii, jj, next, s, ret);
      sub += cur;
    }

    if (!(val -= sub)) tn->children.erase(c);
    s.pop_back();
    board[i][j] = c;
    return sub;
  }

 public:
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    for (const string& w : words) add(&trie, w, 0);

    vector<string> ret;
    string temp;
    m = board.size(), n = board[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) work(board, i, j, &trie, temp, ret);
    return ret;
  }
};
