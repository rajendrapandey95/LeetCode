class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        ans = n * 2
        reservedSeats.sort()

        i = 0
        while i < len(reservedSeats):
            curr = reservedSeats[i][0]
            flag25 = 1
            flag47 = 1
            flag69 = 1

            while i < len(reservedSeats) and reservedSeats[i][0] == curr:
                seat = reservedSeats[i][1]

                if 2 <= seat <= 5:
                    flag25 = 0
                    if 4 <= seat <= 5:
                        flag47 = 0

                elif 6 <= seat <= 9:
                    flag69 = 0
                    if 6 <= seat <= 7:
                        flag47 = 0

                i += 1

            if flag69 == 0 and flag25 == 0 and flag47 == 0:
                ans -= 1
                ans -= 1
            elif flag69 == 0 or flag47 == 0 or flag25 == 0:
                ans -= 1

        return ans
