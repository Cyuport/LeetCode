class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reversePrint(head: ListNode) -> [int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    res.reverse() #list的reverse()没有返回值
    return res