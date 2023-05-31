# Validate ip address

[Problem link](https://leetcode.com/problems/validate-ip-address)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/validate-ip-address

class Solution {
 public:
  bool validhex(char c) {
    return (c >= '0' and c <= '9') or (c >= 'a' and c <= 'f') or
           (c >= 'A' and c <= 'F');
  }
  bool validIPv6Address(string IP) {
    string piece = "";
    int cnt = 0, l = 0;
    for (char c : IP) {
      if (c == ':') {
        if (++cnt == 8 or l == 0) return false;
        l = 0;
      } else if (validhex(c)) {
        if (++l > 4) return false;
      } else
        return false;
    }
    return cnt == 7 and l > 0;
  }
  bool validIPv4Address(string IP) {
    string piece = "";
    int cnt = 0, l = 0, cur = 0;
    for (char c : IP) {
      if (c == '.') {
        if (++cnt == 4 or l == 0) return false;
        l = 0;
        cur = 0;
      } else if (c >= '0' and c <= '9') {
        if (++l > 1 and cur == 0) return false;
        if ((cur = cur * 10 + c - '0') > 255) return false;
      } else
        return false;
    }
    return cnt == 3 and l > 0;
  }
  string validIPAddress(string IP) {
    if (validIPv4Address(IP))
      return "IPv4";
    else if (validIPv6Address(IP))
      return "IPv6";
    else
      return "Neither";
  }
};
```