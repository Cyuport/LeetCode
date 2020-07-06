def canFinish(numCourses: int, prerequisites: [[int]]) -> bool:
    indegrees = [0 for _ in range(numCourses)]
    adjacency = [[] for _ in range(numCourses)]
    queue = []
    count = numCourses
    for cur, pre in prerequisites:
        indegrees[cur] += 1
        adjacency[pre].append(cur)
    for i in range(numCourses):
        if not indegrees[i]:
            queue.append(i)
            count -= 1
    while queue:
        pre = queue.pop(0)
        for cur in adjacency[pre]:
            indegrees[cur] -= 1
            if not indegrees[cur]:
                queue.append(cur)
                count -= 1
    return not count


if __name__ == '__main__':
    print(canFinish(2, [[1,0],[0,1]]))
