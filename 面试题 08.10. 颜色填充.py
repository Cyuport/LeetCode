def floodFill(image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
    target = image[sr][sc]
    r, c = len(image), len(image[0])
    if target == newColor:
        return image
    def helper(i: int, j: int):
        image[i][j] = newColor
        if i < r-1 and image[i+1][j] == target:
            helper(i+1,j)
        if i > 0 and image[i-1][j] == target:
            helper(i-1,j)
        if j < c-1 and image[i][j+1] == target:
            helper(i,j+1)
        if j > 0 and image[i][j-1] == target:
            helper(i,j-1)

    helper(sr,sc)
    return image