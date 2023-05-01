// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution {
 public:
  double average(vector<int>& salary) {
    double tot = salary[0], small = tot, big = tot;
    int n = salary.size();
    for (int i = 1; i < n; ++i) {
      double x = salary[i];
      tot += x;
      small = min(small, x);
      big = max(big, x);
    }
    return (tot - small - big) / (n - 2);
  }
};
