// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings

class Solution {
 public:
  vector<int> maxDepthAfterSplit(string seq) {
    vector<int> ret;
    int prefix = 0;
    for (char c : seq) ret.push_back((c == '(' ? prefix++ : --prefix) & 1);
    return ret;
  }
};
