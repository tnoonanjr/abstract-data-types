class Stack:
  ''' 
  Bare-bones stack object. The 'pop' method is LIFO: last in, first out.
  
  '''
  def __init__(self):
    self._L = []
 
  def push(self, item):
    self._L.append(item)
 
  def pop(self):
    return self._L.pop() if not self.is_empty() else None
  
  def peek(self):
     if not self.is_empty():
        return self._L[0]
  
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
       