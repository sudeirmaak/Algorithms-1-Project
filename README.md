# Assignment 1

## Task 1: "Ordnung must sein” 3-4
* A. Implement bubble sort, insertion sort, merge sort, quick sort. Test and compare their
running times for a number of
** • small (ca. 5–50) and
** • large input sizes.
Carefully choose (or even average) appropriate inputs to ensure you justify the right
conclusion. Include a graph with the results of your measurements for all algorithms, e.g.
running time as a function of array size.

* B. The Olsen Gang has obtained a set of 20k credit card details. Unfortunately, when
transferring through the dark web, due to a sloppy internet connection, the data set got
split into two parts. Moreover, the card records in the second part got randomly shuffled,
so, before they can sell the data for big money, they must match them up with card
numbers from the first part. Luckily, this is possible, as it is known that the records in the
first dataset go in the order of increasing expiration dates and the PIN. Choose a linear
time algorithm for the job and help the gand cash out.
Empirically investigate at what data volume the linear solution gains supremacy over a
log-linear algorithm.

# Assignment 2

## Task 1: ”An Introduction to Applied Dendrology” 3
Implement a binary tree-based container for say integers. Draw a large set of random
keys. Empirically compare the cumulative running times for inserting the keys into:
* a) a binary tree, in the original random order,
* b) a binary tree, in the best-case order of, e.g. building consecutive levels of the
tree downwards. Root, its children, grandchildren ... (requires rearranging the keys
beforehand),
Explanation: the goal is to obtain a perfectly balanced tree, thus no node can be
inserted before its parent in the balanced version of the tree. You may assume that
you have 𝑛=2^m -1 keys.
* c) a library solution, say std::set.

## Task 2: "Pruning the bushes” 4
Include in Task 1 a comparison of key removal times for the two data structures, say, in
original random order.
