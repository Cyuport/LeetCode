def KCloset(points: [[int]], K: int) -> [[int]]:
    distance = {i: points[i][0]**2+points[i][1]**2 for i in range(0, len(points))}
    distance = sorted(distance.items(), key=lambda d: d[1])
    res = []
    for i in range(0, K):
        res.append(points[distance[i][0]])
    return res


if __name__ == '__main__':
    points = [[1, 3], [-2, 2], [3,3]]
    K = 1
    print(KCloset(points, K))


