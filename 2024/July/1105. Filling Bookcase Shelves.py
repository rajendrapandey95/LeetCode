class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = [[0] * (shelfWidth + 1) for _ in range(len(books))]
        return self.dp(books, shelfWidth, memo, 0, shelfWidth, 0)

    def dp(self, books, sw, memo, i, rem_w, mh):
        cur = books[i]
        mh_upd = max(mh, cur[1])
        if i == len(books) - 1:
            return mh_upd if rem_w >= cur[0] else mh + cur[1]
        if memo[i][rem_w] != 0:
            return memo[i][rem_w]
        opt1 = mh + self.dp(books, sw, memo, i + 1, sw - cur[0], cur[1])
        if rem_w >= cur[0]:
            opt2 = self.dp(books, sw, memo, i + 1, rem_w - cur[0], mh_upd)
            memo[i][rem_w] = min(opt1, opt2)
            return memo[i][rem_w]
        memo[i][rem_w] = opt1
        return memo[i][rem_w]
