def findOrder(numCourses: int, prerequisites: [[int]]) -> [int]:
    indegrees = [0 for _ in range(numCourses)]
    adjacency = [[] for _ in range(numCourses)]
    queue = []
    count = numCourses
    order = []
    for cur, pre in prerequisites:
        indegrees[cur] += 1
        adjacency[pre].append(cur)
    for i in range(numCourses):
        if not indegrees[i]:
            queue.append(i)
            count -= 1
    while queue:
        pre = queue.pop(0)
        order.append(pre)
        for cur in adjacency[pre]:
            indegrees[cur] -= 1
            if not indegrees[cur]:
                queue.append(cur)
                count -= 1
    if count:
        return []
    return order


if __name__ == '__main__':
    print(findOrder(2, [[1,0]] ))