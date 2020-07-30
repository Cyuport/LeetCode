import collections

def findWhetherExistsPath(n: int, graph: [[int]], start: int, target: int) -> bool:
    neibor = collections.defaultdict(set)
    for key, value in graph:
        neibor[key].add(value)
    visited = [False]*n

    def dfs(start: int, target: int, visited) -> bool:
        if start == target:
            return True
        if visited[start]:
            return False
        visited[start] = True
        ans = False
        if start in neibor:
            for next in neibor[start]:
                ans = ans or dfs(next, target, visited)
        return ans

    return dfs(start,target,visited)

