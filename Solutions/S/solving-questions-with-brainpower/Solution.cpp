// https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution {
 public:
  long long mostPoints(vector<vector<int>>& questions) {
    int n = questions.size();
    vector<long long> best(n + 1);
    for (int i = n - 1; i >= 0; --i)
      best[i] = max(best[i + 1],
                    questions[i][0] + best[min(n, i + questions[i][1] + 1)]);
    return best[0];
  }
};
