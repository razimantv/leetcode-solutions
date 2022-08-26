// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string

class Solution {
 public:
  string evaluate(string s, vector<vector<string>>& knowledge) {
    map<string, string> dict;
    for (const auto& v : knowledge) {
      dict[v[0]] = v[1];
    }

    string ret = "", cur = "";
    for (bool in = false; char c : s) {
      if (c == '(') {
        cur = "";
        in = true;
      } else if (c == ')') {
        if (dict.count(cur))
          ret += dict[cur];
        else
          ret += '?';
        in = false;
      } else if (in)
        cur += c;
      else
        ret += c;
    }
    return ret;
  }
};
