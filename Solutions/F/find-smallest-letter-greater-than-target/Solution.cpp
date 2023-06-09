// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution {
 public:
  char nextGreatestLetter(vector<char>& letters, char target) {
    auto vit = upper_bound(letters.begin(), letters.end(), target);
    return vit == letters.end() ? letters[0] : *vit;
  }
};
