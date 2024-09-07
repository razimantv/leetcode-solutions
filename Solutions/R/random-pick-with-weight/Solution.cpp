// https://leetcode.com/problems/random-pick-with-weight

class Solution {
 public:
  map<int, int> wmap;
  int tot;

  Solution(vector<int>& w) {
    tot = 0;
    for (int i = 0; i < w.size(); i++) {
      if (w[i] == 0) continue;
      wmap[tot += w[i]] = i;
    }
  }

  int pickIndex() { return wmap.lower_bound(rand() % tot + 1)->second; }
};

