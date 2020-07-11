class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Node) -> Node:
    if not head:
        return None
    visited = {}
    def dfs(head: Node):
        if not head:
            return None
        if head in visited:
            return visited[head]
        node = Node(head.val)
        visited[head] = node
        node.next = dfs(head.next)
        node.random = dfs(head.random)
        return node
    dfs(head)
    return visited[head]