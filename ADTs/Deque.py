class Deque: 
    '''
    A Deque is a double-sided queue that can push and pop items from both sides.

    
    Deques initialize with two instance variables:
        - An empty list in which items will be pushed.
        - A private length variable that will be manually updated.

        
    The length method will simply return the instance variable.

    
    To ensure the deque is not empty:
        - Return a boolean indicating if the length is 0.


    To push to the **beginning** of the deque:
        - Update the length.
        - Insert a new item at the front of the list.
    
        
    To push to the **end** of the deque:
        - Update the length.
        - Insert a new item at the back of the list.

        
    To pop from the **beginning** of the deque:
        - Update the length.
        - Pop an item from the front of the list.

        
    To pop from the **end** of the deque:
        - Update the length.
        - Pop an item from the back of the list.
    
        
    To peek at the item in the front of the deque:
        - Ensure the deque is not empty.
        - Return the item at the front of the list.

    
    '''
    def __init__(self):
        self._L = []
        self._len = 0
    
    def __len__(self):
        return self._len
    
    def is_empty(self):
        return len(self._L) == 0
    
    def push_front(self, item):
        self._len += 1
        self._L.insert(0, item)
        
    
    def push_last(self, item):
        self._len += 1
        self._L.append(item)
    
    def pop_front(self):
        if not self.is_empty():
            self._len -= 1
            return self._L.pop()
        return None
    
    def pop_last(self):
        if not self.is_empty():
            self._len -= 1
            return self._L.pop(0)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self._L[0]
        return None
    
    

if __name__ == '__main__':
    deque = Deque()
    print(f"Deque empty: {deque.is_empty()}") 

    n = 9
    for i in range(n):
        print(f"Appending: {i}")
        deque.push_last(i)
    print(f"Inserting 'front' at index 0")
    deque.push_front('front')

    print(f"Deque empty: {deque.is_empty()}") 
    print(f"Deque size: {deque._len}")  
    print(f"Removing Front: {deque.pop_front()}")  
    print(f"Removing Rear item: {deque.pop_last()}")    
    