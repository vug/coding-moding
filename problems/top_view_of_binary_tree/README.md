A problem that me and Steve worked together on 2019-04-27.

- [Print Nodes in Top View of Binary Tree \- GeeksforGeeks](https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/)
- [Print nodes in top view of Binary Tree \| Set 2 \- GeeksforGeeks](https://www.geeksforgeeks.org/print-nodes-in-top-view-of-binary-tree-set-2/)

Given a binary tree data structure, assume root node is at `(x, y) = (0, 0)` coordinate. And right child's `x` coordinate is `x + 1` of partent's coordinate (similarly, left child is `x - 1`) and children's `y` coordinate is `y + 1` of parent's. The goal is to get the list of top most node values sorted in positive x direction.

Assuming that we know how to traverse a binary tree, first initial brute for reaction was to iterate over nodes and bucket/group them according to their x coordinate. (O(N)) Then go over each bucket in increasing x order, and find the node with smallest y-coordinate and append its value in an array.

When started to implement, I realized we don't need to keep the whole bucket but for each x-coordinate keep the node with minimum y value. 

The data structure to hold the top-view state while traversing is a dict from int (x-coord) to a tuple (y-coord, Node). Actually the second element of the tuple does not have to be the node itself, but its value, but I used the whole Node, becase I wanted to learn more about complex C++ data types.

We solved the problem in Python and C++. ^_^

Steve came up with the idea of generalizing the question to left, right and bottom view. For which bucketing has to be done by x or y coordinate, and choose nodes with either minimum or maximum y/x value.