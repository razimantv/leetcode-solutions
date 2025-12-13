# https://leetcode.com/problems/coupon-code-validator/

class Solution:
    def validateCoupons(
        self, codes: list[str], lines: list[str], actives: list[bool]
    ) -> list[str]:
        return [c for l, c in sorted([
            (line, code)
            for code, line, active in zip(codes, lines, actives) if (
                active and code and
                line in [
                    "electronics", "grocery", "pharmacy", "restaurant"
                ] and
                ('a' + code).isidentifier()
            )
        ])]
