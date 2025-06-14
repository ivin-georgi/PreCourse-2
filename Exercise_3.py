# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        

    def push(self, new_data): 
        '''
        TC: O(1)
        '''
        temp = Node(new_data)

        if self.head is None:
            self.head = temp
            return 
        
        curr = self.head
        self.head = temp
        self.head.next = curr
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        '''
        TC: O(n)
        '''
        curr = self.head
        if curr == None:
            return None
        slow = curr
        fast = curr
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
