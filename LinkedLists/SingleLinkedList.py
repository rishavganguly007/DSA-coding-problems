# Linked List
class Node:
    val: int
    next: 'Node'

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
  head:Node # holds the addres of the first element
  tail:Node # holds the address of the last element
  size: int # holds the size of the linked-list
  def __init__(self) -> None:
      self.size = 0
      self.head = None
      self.tail = None

  #Inserts the Node at from the beginning
  def insertFirst(self, val= 0):
      temp = Node(val)
      temp.next = self.head
      self.head = temp
      if self.tail == None:
        self.tail = self.head
      self.size += 1
  
  # inserts a node at the end
  def insertBack(self, val = 0):
      if self.head == None:
        self.insertFirst(val)
        return
      
      node = Node(val)
      self.tail.next = node
      self.tail = node
      self.size += 1

  #inserts a node at any given position
  def insert(self, val, index):
    #TO-DO: check condition for Index > size
      if index == 1:
        self.insertFirst(val)
        return
      if index == self.size:
        self.insertBack(val)
        return

      temp = self.head
      for i in range(1, index -1):
        temp = temp.next
      node = Node(val, temp.next)
      temp.next = node
      self.size += 1
      return 

  def deleteFirst(self) -> int:
    value = self.head.val #stroes the value to be deleted
    # head takes the address of the next node; 
    # like 2-> 3-> 4; head takes the adress of 3
    self.head = self.head.next 
    if self.head == None: #if only single element was present
      self.tail = None
    self.size -= 1
    return value

  def deleteLast(self) -> int:
    if self.size <= 1:
      self.deleteFirst()
    
    # gets the index of the 2nd last node, 
    # as it's needed for the singly list as it can only traverse fotward
    secondLast: Node = self.getNodeIndex(self.size - 1) 
    value = secondLast.val
    tail = secondLast
    tail.next = None
    self.size -= 1
    return

  def deleteAny(self, index: int):
    if index == 1:
      self.deleteFirst()
      self.size -= 1
      return
    if index == self.size:
      self.deleteLast()
      self.size -= 1
      return
    previous_node: Node = self.getNodeIndex(index - 1) # gets element previous to the one that is to be deleted
    value = previous_node.next.val
    previous_node.next = previous_node.next.next
    self.size -=1 
    return value
  
  def getNodeIndex(self, index) -> Node:
    node: Node = self.head
    for i in range(1, index):
      node = node.next
    return node
    


  def display(self):
    temp : Node = self.head
    while (temp != None):
      print(temp.val, "-> ", end ="")
      temp = temp.next
    print("None")
  
ll = LinkedList()
ll.insertBack(2)
ll.insertBack(3)
ll.insertBack(4)
ll.insertBack(5)
ll.insertBack(6)
ll.insert(7, 6)
ll.display()
ll.deleteFirst()
ll.display()
ll.deleteLast()
ll.display()
ll.deleteAny(2)
ll.display()

  

