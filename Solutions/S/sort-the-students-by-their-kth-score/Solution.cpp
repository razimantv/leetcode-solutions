// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution {
 public:
  vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
    sort(score.begin(), score.end(),
         [&](auto& a, auto& b) { return a[k] > b[k]; });
    return score;
  }
};
