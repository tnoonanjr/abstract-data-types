class Queue:
    ''' 
    The Queue abstract data type is FIFO: first in, first out. It will 
    push items to the end and pop them from the front

    
    Queues initialize with one instance variable:
        - An empty list in which items will be pushed

        
    The length method simply returns length of the instance variable

    
    To ensure the deque is not empty:
        - Return a boolean indicating if the length is 0

          
    To push to the **end** of the queue:
        - Insert a new item at the back of the list

        
    To pop from the **beginning** of the queue:
        - Ensure the instance is not empty
        - Pop an item from the front of the list

           
    To peek at the item in the front of the queue:
        - If the instance is empty return None
        - Return the item at the front of the list

    '''
    def __init__(self):
        self._L = []
    
    def __len__(self):
        return len(self._L)
    
    def is_empty(self):
        return len(self._L) == 0
    
    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        if self.is_empty():
            return IndexError("Cannot pop from empty Queue")
        return self._L.pop(0)
          
    def peek(self):
        if self.is_empty():
            return None
        return self._L[0]
               
    
    
    
if __name__ == '__main__':
    q = Queue()
    n = 10
    for i in range(n):
        print(f"pushing: {i}")
        q.push(i)
    print("Queue:", q._L)
    print(f"Empty? {q.is_empty()}")

    print(f"pop: {q.pop()}")
    print(f"Updated Queue: {q._L}")
    print(f"Peek: {q.peek()}")
    print(f"Queue length: {q._len}")