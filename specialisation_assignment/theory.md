1.1. The deque module is part of which python library?
The deque module is par of the collections module.

1.2. What are 2 differences that distinguish a tree from a graph?
Within a tree there are no cycles present, however with a graph there is the oppurtunity for them to be present or not be present. The paths between nodes also varies, with trees there can only be one unique path between any two nodes, however with a graph there is no restriction, where a graph can have either zero paths or many.

1.3. Give the definitions of time complexity and space complexity.
Time complexity is used to measure the efficiency of a programme, it describes the amount of time using the big O notation that an algorithm takes to fully complete a function. Space complexity similarly also uses the big O notation as a measure for best and worse case scenarios, however with space complecity it describes the amount of memory that an algorithm would take up when the function is fully complete, this is useful as you are able to measure how the size of your algorith is going to effect its efficiency to the user.

1.4. Describe the bubble sort algorithm and its complexity. What is guaranteed at the end of the first pass?
A bubble algorith sorts through a list comparing it to the element in front, the process is repeated so that the list is then ordered correctly and no more swaps are needed. The worst case scenario for time complexity within a bubble sort would be O(n2) where all elements places need to be sorted, if they are in reverse order, meaning that if every element needs to be moved it means going through the whole set of data until all elements are swapped. The space complexity would be O(1) due to not needing any extra space, as it swaps each element with another already existing element.

1.5. Explaing what LIFO and FIFO are and how each works in practice with a named data structure.
LIFO is an acronym for last-in-first-out, meaning that the last item that was added, will be the first to be removed, operations that adopt this concept would be 'pop' which removes the item from the top. The use of this concept wuold be to undo functionality within many applications. The named data structure it would work within would be a stack, the 'pop' function would always remove the last element from the top, and the stack can be implemented using linked lists or arrays.

FIFO is an acronmy for first-in-first-out, meaning that the first item to be added is the first item that will be removed. operations that adopt this concept would be 'dequeue' which removes the item from the front of the queue. The use of this concept would be order processing, in the case where the first order needs to be processed first. The named data structure of a queue could use dequeue to remove the element from the front, this queue could be implemented using linked, lists arrays or multiple stacks.

1.6. What is a Balanced Binary Tree and what would be the best root? Walkthrough how you search using this structure.
A balanced binary tree is where the two subtrees of every node only differ by one, and no more, this can be done with the use of an AVL tree which re-balances the tree if the subtrees differ by anymore than one. The best choice for the root would be middle element if you are working with a list of sorted elements, as this would ensure that only both sides of the tree they would be evenly distributed.
The process of searching using this structure would start at the root, you would compare the search key with the key of the current node, there would then be three potential outcomes to this, that either the search key is equal to the key in the current node, the search is less than where it sits on the left hand side of the tree or it is more than and sits on the right hand side of the tree.


