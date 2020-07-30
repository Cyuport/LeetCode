class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def partition(head: ListNode, x: int) -> ListNode: #快排的分割，双指针
    i = head
    index = head
    while i:
        if i.val < x:
            index.val, i.val = i.val, index.val
            index = index.next
        i = i.next
    return head