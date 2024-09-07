// https://leetcode.com/problems/iterator-for-combination

class CombinationIterator {
 public:
  vector<int> perm;
  bool can;
  string word;
  CombinationIterator(string characters, int k) {
    word = characters;
    perm = vector<int>(word.size(), 0);
    fill(perm.begin(), perm.begin() + k, 1);
    can = true;
  }

  string next() {
    string ret = "";
    for (int i = 0; i < perm.size(); ++i)
      if (perm[i]) ret += word[i];
    can = prev_permutation(perm.begin(), perm.end());
    return ret;
  }

  bool hasNext() { return can; }
};

