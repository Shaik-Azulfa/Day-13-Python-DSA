#Middle element of Linked List
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function should return data of middle node
    # If even length, return second middle
    def findMid(self, head):
        """
        Time: O(n) | Space: O(1)
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.data
      # Node Class
#Loop of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to check if linked list has a loop
    def detectLoop(self, head):
        """
        Floyd's Cycle Detection Algorithm
        Time: O(n) | Space: O(1)
        """
        if head is None or head.next is None:
            return False
            
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False
