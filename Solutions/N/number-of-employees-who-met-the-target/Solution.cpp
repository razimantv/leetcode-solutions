// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
 public:
  int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
    int ret{};
    for (int x : hours) ret += (x >= target);
    return ret;
  }
};
