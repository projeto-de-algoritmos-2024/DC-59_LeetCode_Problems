class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
    
    def merge1(self, l, r):
        if not l or not r:
            return l or r
        if l.val < r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r

######### FUNÇÕES PARA RODAR LOCAL FORA DO LEETCODE ############
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Examples
solution = Solution()

lists1 = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]
result1 = solution.mergeKLists(lists1)
print("Example 1 Result:", linked_list_to_list(result1))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

lists2 = []
result2 = solution.mergeKLists(lists2)
print("Example 2 Result:", linked_list_to_list(result2))  # Output: []

lists3 = [create_linked_list([])]
result3 = solution.mergeKLists(lists3)
print("Example 3 Result:", linked_list_to_list(result3))  # Output: []
