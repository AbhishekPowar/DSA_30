# 5__Grid_Unique_Paths


# My Idea
def orignal(m, n):
    def isvalid(x, y, m, n):
        return not(x >= m or y >= n)

    from functools import lru_cache

    @lru_cache(100)
    def paths(x, y, m, n):
        if x == m-1 and y == n-1:
            return 1
        elif x >= m or y >= n:
            return None
        else:
            fy = 0
            fx = 0
            s = 0
            if isvalid(x, y+1, m, n):
                s += paths(x, y+1, m, n)
            if isvalid(x+1, y, m, n):
                s += paths(x+1, y, m, n)
            # s += 1
            return s

    matrix = [[f'{i}{j}' for j in range(m)] for i in range(n)]
    matrix2 = [[f'{i}{j}' for j in range(m)] for i in range(n)]
    # print(*matrix,sep='\n')
    d = {}
    for x in range(n):
        for y in range(m):
            ans = paths(x, y, n, m)
            matrix2[x][y] = str(ans).zfill(2)
    print()
    print(*matrix2, sep='\n')
    return int(matrix2[0][0])

# DP O(n)
# space O(m*n)


def dp(m, n):
    mat = [[1 if i == 0 or j == 0 else 0 for i in range(m)] for j in range(n)]
    for y in range(1, m):
        for x in range(1, n):
            mat[x][y] = mat[x-1][y] + mat[x][y-1]
    return mat[n-1][m-1]

# DP m*n
# Space O(n)


def Dp(m, n):
    def uniquePaths(m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        return dp[-1]
    return uniquePaths(m, n)


#  Math solution
def Math(m, n):
    def nCr(n, r):
        r = max(r, n-r)
        num = 1
        for i in range(r+1, n+1):
            num *= i
        r = min(r, n-r)
        den = 1
        for j in range(2, r+1):
            den *= j
    return num//den

    return nCr(m+n-2, min(m, n)-1)


if __name__ == "__main__":
    m, n = 6, 4
    ans = dp(m, n)
