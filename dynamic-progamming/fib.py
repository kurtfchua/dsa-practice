# fibonacci -> dp
def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = memoization(n-1, cache) + memoization(n-2, cache)

    return cache[n]

def dp(n):
    if n <= 1:
        return n
    
    dp = [0,1]
    i = 2
    while i <= n:
        dp[0], dp[1] = dp[1], dp[1] + dp[0]
        i += 1

    return dp[1]

# graph dfs -> dp
def dfs(r, c, ROWS, COLS):
    if r == ROWS or c == COLS:
        return 0 
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    return dfs(r+1, c, ROWS, COLS) + dfs(r, c+1, ROWS, COLS)

def memoization(r, c, ROWS, COLS, cache):
    if r == ROWS or c == COLS:
        return 0 
    if cache[r][c] > 0: 
        return cache[r][c]
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    cache[r][c] = memoization(r+1, c, ROWS, COLS) + memoization(c, c+1, ROWS, COLS)

    return cache[r][c]

def dp(rows, cols):
    # initiate prev row
    prev_row = [0 for _ in range(cols)]

    for _ in range(rows-1, -1, -1):
        current_row = [0 for _ in range(cols)]
        current_row[cols-1] = 1
        for c in range(cols-2, -1, -1):
            current_row[c] = current_row[c+1] + prev_row[c]
        prev_row = current_row
    
    return prev_row[0]
        

cache = [[0]*4 for _ in range(4)]
cache = [[0 for _ in range(4)] for _ in range(4)]