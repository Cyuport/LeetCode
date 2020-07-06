class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True
    slow, fast = head, head
    reversed_head = None
    while fast and fast.next:
        tmp = slow
        slow = slow.next
        fast = fast.next.next
        tmp.next = reversed_head
        reversed_head = tmp
    if fast:
        slow = slow.next
    while slow and reversed_head:
        if slow.val != reversed_head.val:
            return False
        slow = slow.next
        reversed_head = reversed_head.next
    return True

