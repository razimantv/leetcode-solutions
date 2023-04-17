// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution {
 public:
  vector<bool> kidsWithCandies(vector<int>& candies, int extra) {
    int m = *max_element(candies.begin(), candies.end());
    vector<bool> ret;
    for (int x : candies) ret.push_back(x + extra >= m);
    return ret;
  }
};
