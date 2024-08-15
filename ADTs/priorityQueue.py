class PriorityQueue:
    ''' 
    Priority queues are queues with a special queue that gives each 
    element an associated priority. They are  most commonly implemented 
    in heaps. This implementation is a max-priority queue, It will 
    prioritize popping higher values first.
        
    
    Priority queues initialize with **one instance variable**:
        - an empty list in which items will be pushed.

      
    I decided to give my PriorityQueue a **string representation**. This is not 
    necessarily required but it is helpful for testing.

    
    The length method simply returns length of the instance variable.


    To ensure the stack is not empty:
        - Return a boolean indicating if the length is 0.
    
        
    To push an element to a priority queue:
        - append the element to the list

        
    To pop an element from a priority queue:
        - ensure the instance is **not** empty
        - set the current index as the **maximum** value
        - **loop** over the list and find the maxmimum element
        - **return and pop** the maxmimum element

    '''
    def __init__(self):
        self._L = []

    def __repr__(self):
        return f"PriorityQueue: {self._L}"
    
    def __len__(self):
        return len(self._L)
    
    def is_empty(self):
        return len(self._L) == 0

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty PriorityQueue")
        max_idx = 0
        for i in range(len(self._L)):
            if self._L[i] > self._L[max_idx]:
                max_idx = i
        return self._L.pop(max_idx)



if __name__ == '__main__':
    pq = PriorityQueue()

    pq.push(9)
    pq.push(5)
    pq.push(42)
    pq.push(1)
    pq.push(10)
    print(pq)
    print(f"Empty? {pq.is_empty()}")
    print(f"Length: {len(pq)}")

    # Expected to pop the maximum value pushed
    while not pq.is_empty():
        popped_pq = pq.pop()
        print(f"Popped: {popped_pq}")
    print(f"Empty? {pq.is_empty()}")