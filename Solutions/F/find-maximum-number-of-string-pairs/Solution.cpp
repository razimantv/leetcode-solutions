// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution {
 public:
  int maximumNumberOfStringPairs(vector<string>& words) {
    unordered_set<string> seen;
    int ret{};
    for (auto w : words) {
      if (seen.count(w)) ++ret;
      reverse(w.begin(), w.end());
      seen.insert(w);
    }
    return ret;
  }
};
