class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0

        for customer_bill in bills:
            if customer_bill == 5:
                five_dollar_bills += 1
            elif customer_bill == 10:
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    return False
            else:  # customer_bill == 20
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
        return True
