// https://leetcode.com/problems/split-with-minimum-sum/

class Solution {
 public:
  int splitNum(int num) {
    auto s = to_string(num);
    sort(s.begin(), s.end());
    int L{}, R{};
    for (char c : s) {
      L = L * 10 + c - '0';
      swap(L, R);
    }
    return L + R;
  }
};
