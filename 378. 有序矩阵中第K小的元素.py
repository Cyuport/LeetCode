def kthSmallest(matrix:[[int]], k: int) -> int:
    n = len(matrix)
    return sorted([matrix[i][j] for i in range(n) for j in range(n)])[k-1]