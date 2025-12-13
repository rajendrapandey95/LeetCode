from typing import List

class Solution:
    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool]
    ) -> List[str]:

        n = len(code)

        business_line_order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        sortable_coupons = []

        for i in range(n):
            if not isActive[i]:
                continue

            if businessLine[i] not in business_line_order:
                continue

            if not code[i]:
                continue

            valid_code = True
            for c in code[i]:
                if not (c.isalnum() or c == "_"):
                    valid_code = False
                    break

            if not valid_code:
                continue

            sort_index = business_line_order[businessLine[i]]
            sortable_coupons.append(((sort_index, code[i]), code[i]))

        sortable_coupons.sort()

        return [entry[1] for entry in sortable_coupons]
