// https://leetcode.com/problems/distribute-candies

class Solution {
 public:
  int distributeCandies(vector<int>& candyType) {
    int n = candyType.size(), types = 1;
    sort(candyType.begin(), candyType.end());

    for (int i = 1; i < n; ++i)
      if (candyType[i] != candyType[i - 1]) ++types;
    return min(types, n / 2);
  }
};
