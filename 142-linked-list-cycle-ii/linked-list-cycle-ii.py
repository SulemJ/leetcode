# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # idx=-1
        dummy = ListNode(None)
        dummy.next=head
        cur = dummy
        b=[]
        # b= []3 2 0 -4
        # idx=0 1 2 3
        while cur.next:
            m=(cur.val,cur.next,cur.next.val)
            if m in b:
                return cur 
            b.append(m)
            # idx+=1
            cur = cur.next
            # if idx > len(b):
            #     return True
        return None