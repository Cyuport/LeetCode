class ListNode:
   def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    root = ListNode(0)
    pos = root
    while l1 and l2:
        if l1.val < l2.val:
            pos.next = ListNode(l1.val)
            l1 = l1.next
        else:
            pos.next = ListNode(l2.val)
            l2 = l2.next
        pos = pos.next
    while l1:
        pos.next = ListNode(l1.val)
        l1 = l1.next
        pos = pos.next
    while l2:
        pos.next = ListNode(l2.val)
        l2 = l2.next
        pos = pos.next
    root = root.next
    return root
