// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix {
 public:
  unordered_set<int> seen;
  int good;
  LUPrefix(int n) : good(0) {}

  void upload(int video) {
    seen.insert(video);
    if (video == 1 or good == video - 1) {
      while (seen.count(video)) good = video++;
    }
  }

  int longest() { return good; }
};

