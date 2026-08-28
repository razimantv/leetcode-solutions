# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        middle = [c for c, x in cnt.items() if x & 1]
        if len(middle) > 1:
            return ''
        elif middle:
            cnt[middle[0]] -= 1
        chars = SortedList(
            sum(([c] * (x // 2) for c, x in cnt.items()), start=[])
        )

        def largest_palindrome(left, chars, middle):
            right = ''.join(chars)
            return ''. join([left, right[::-1], *middle, right, left[::-1]])

        def smallest_palindrome(left, chars, middle):
            right = ''.join(chars)
            return ''. join([left, right, *middle, right[::-1], left[::-1]])

        if largest_palindrome('', chars, middle) <= target:
            return ''

        left = ''
        for c in target[:len(target) // 2]:
            print(left, middle, chars)
            if c in chars:
                chars.remove(c)
                if largest_palindrome(left + c, chars, middle) > target:
                    left += c
                    continue
                chars.add(c)
            d = chars[chars.bisect_right(c)]
            chars.remove(d)
            left += d
            break

        return smallest_palindrome(left, chars, middle)
