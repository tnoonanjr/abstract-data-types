class Stack:
  ''' 
  The stack data type is LIFO: last in, first out.
  
  Stacks initialize with two instance variables:
    - An empty list in which items will be pushed.
    - A private length variable that will be manually updated.

        
  The length method will simply return length of the instance variable.

    
  To ensure the stack is not empty:
    - Return a boolean indicating if the length is 0.

          
  To push to the **end** of the stack:
    - Insert a new item at the back of the list.

        
  To pop from the **beginning** of the stack:
    - Pop an item from the front of the list.

           
  To peek at the item in the front of the stack:
    - Ensure the stack is not empty.
    - Return the item at the front of the list. 
  '''
  def __init__(self):
    self._L = []
  
  def __len__(self):
    return len(self._L)
  
  def push(self, item):
    self._L.append(item)
 
  def pop(self):
    if not self.is_empty():
      return self._L.pop(0)  
    return None
  
  def peek(self):
    if self.is_empty():
      raise IndexError("You cannot peek into an empty stack")
    return self._L[-1]
  
  def is_empty(self):
        return len(self._L) == 0

if __name__ == '__main__': 
    s = Stack()
    n = 10
    for i in range(n):
       s.push(i)
    print(f"Stack: {s._L}")
    
    for i in range(n+1):
       print(f"Popping: {s.pop()}")
       