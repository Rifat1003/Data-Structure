class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p

from typing import Counter
class DoublyList:

  def __init__(self, a):

    self.head = Node(None, None, None)
    self.head.next= self.head.prev= self.head
    tail = self.head 

    for i in range(len(a)):
      new_node = Node(a[i],None,None)
      new_node.next = self.head
      new_node.prev = tail 
      tail.next = new_node
      self.head.prev = new_node
      tail = new_node

    

  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array.
    #self.head = None
  
  
  # Counts the number of Nodes in the list
  def countNode(self):

    temp = self.head.next 

    count = 0 
    
    while (temp != self.head):

      temp = temp.next

      count += 1

    return count

  
  # prints the elements in the list
  def forwardprint(self):
    temp_1 = self.head.next 


    while (temp_1 != self.head):

      print(temp_1.element, end=" ")

      temp_1 = temp_1.next
    print('\n')
    


  # prints the elements in the list backward
  def backwardprint(self):

    temp_2 = self.head.prev

    while( temp_2 != self.head):

      print (temp_2.element, end=" ")
      temp_2 = temp_2.prev

    print('\n')


  # returns the reference of the at the given index. For invalid index return None.

  def nodeAt(self, idx):

    if (idx<0 or idx >= self.countNode()):
      print("Invalid index") 

    temp_3 = self.head.next

    count = 0

    while count < idx:
      temp_3 = temp_3.next
      count +=1
    
    return temp_3
   

  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    count = 0
    temp = self.head
    while temp.next.element!=elem:
      temp=temp.next
      count+=1
    return count

  # inserts containing the given element at the given index Check validity of index.

  def insert(self, elem, idx):
    
    temp = self.head.next
    newnode = Node(elem,None,None)
    
    i = 0
    while i < idx:
      temp = temp.next
      i+=1
    current = temp
    current_2 = temp.prev
    current.prev = newnode
    newnode.next = current
    newnode.prev = current_2
    current_2.next = newnode

    
  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.

  def remove(self, idx):
    temp = self.head
    i = 0
    while i<=idx:
      temp = temp.next
      i+=1
    current = temp.next
    current_2 = temp.prev
    current_2.next = current
    current.prev = current_2
    
    return str(temp.element)




print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.
