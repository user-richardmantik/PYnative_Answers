dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

memo = {}

for i in dist:
    for j in dist[i]:
        if (i not in memo.keys()):
            memo[i] = {}
        elif (j not in memo[i].keys()):
            memo[i][j] = dist[i][j]
        else:
            memo[n][j] = min(memo[n][j], memo[n][i] + memo[i][j])

# TO DO: