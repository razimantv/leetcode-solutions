// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution {
 public:
  int minPartitions(string n) {
    return (*max_element(n.begin(), n.end())) - '0';
  }
};
