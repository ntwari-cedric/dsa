class ListNode:
    def __init__(self,val):
        self.val=val
        self.next= None
        self.prev=  None


class MyLinkedList:

    def __init__(self):
        self.left= ListNode(0)
        self.right= ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if cur and index == 0 and cur!= self.right:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node, next_, prev = ListNode(val), self.left.next, self.left
        next_.prev= new_node
        prev.next= new_node
        new_node.next= next_
        new_node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        new_node, next_, prev = ListNode(val), self.right, self.right.prev
        next_.prev= new_node
        prev.next= new_node
        new_node.next= next_
        new_node.prev = prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index >0:
            cur= cur.next
            index -=1
        if cur and index ==0:
            new_node, next_, prev = ListNode(val), cur, cur.prev
            next_.prev= new_node
            prev.next= new_node
            new_node.next= next_
            new_node.prev = prev
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if cur and index == 0 and cur != self.right:
            next_, prev = cur.next, cur.prev
            prev.next=next_
            next_.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)