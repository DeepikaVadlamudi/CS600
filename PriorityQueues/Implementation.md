# Priority Queues
They support two operations :
- insert(i)
- deleteMin()

## Ways to implement priority queues
- Standard queue
    - insert : O(1)
    - deleteMin() : O(n)
- Ordered Array
   - insert : O(n)
   - deleteMin() : O(1)
 
 
 ### Best way to implement priority queues : Binary Heaps
     - insert : O(logn)
     - deleteMin() : O(logn)
     
  - Binary Heaps are complete Binary trees.
  - Min-heap : parent's key is lesser than or equal to the child's key
  - Max-heap : parent's key is greater than or equal to the child's key
