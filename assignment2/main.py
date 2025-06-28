import random
import time
import csv
import matplotlib.pyplot as plt
from sortedcontainers import SortedSet

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

def generate_random_keys(n):
    return random.sample(range(1, 1000000), n)

def create_balanced_order(keys):
    if not keys:
        return []
    mid = len(keys) // 2
    return [keys[mid]] + create_balanced_order(keys[:mid]) + create_balanced_order(keys[mid+1:])

def measure_time(operation, container, keys):
    start_time = time.perf_counter()
    for key in keys:
        if operation == "insert":
            container.insert(key) if isinstance(container, BST) else container.add(key)
        elif operation == "delete":
            container.delete(key) if isinstance(container, BST) else container.discard(key)
    return (time.perf_counter() - start_time) * 1000

def run_experiment(sizes):
    results = [["Size", "BST_Random_Insert", "BST_Balanced_Insert", "SortedSet_Insert",
                "BST_Random_Delete", "BST_Balanced_Delete", "SortedSet_Delete"]]

    for size in sizes:
        keys = generate_random_keys(size)
        balanced_keys = create_balanced_order(sorted(keys))

        bst_random = BST()
        bst_balanced = BST()
        sorted_set = SortedSet()

        bst_random_insert_time = measure_time("insert", bst_random, keys)
        bst_balanced_insert_time = measure_time("insert", bst_balanced, balanced_keys)
        sorted_set_insert_time = measure_time("insert", sorted_set, keys)

        bst_random_delete_time = measure_time("delete", bst_random, keys)
        bst_balanced_delete_time = measure_time("delete", bst_balanced, balanced_keys)
        sorted_set_delete_time = measure_time("delete", sorted_set, keys)

        results.append([size, bst_random_insert_time, bst_balanced_insert_time, sorted_set_insert_time,
                        bst_random_delete_time, bst_balanced_delete_time, sorted_set_delete_time])

    return results

def save_results_csv(results, filename="table.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(results)

def plot_results(results):
    sizes = [row[0] for row in results[1:]]
    bst_random_insert_times = [row[1] for row in results[1:]]
    bst_balanced_insert_times = [row[2] for row in results[1:]]
    sorted_set_insert_times = [row[3] for row in results[1:]]
    bst_random_delete_times = [row[4] for row in results[1:]]
    bst_balanced_delete_times = [row[5] for row in results[1:]]
    sorted_set_delete_times = [row[6] for row in results[1:]]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, bst_random_insert_times, marker='o', label="BST (Random Order)")
    plt.plot(sizes, bst_balanced_insert_times, marker='s', label="BST (Balanced Order)")
    plt.plot(sizes, sorted_set_insert_times, marker='^', label="SortedSet")
    plt.xlabel("Input Size")
    plt.ylabel("Insertion Time (ms)")
    plt.title("Insertion Time Comparison")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(sizes, bst_random_delete_times, marker='o', label="BST (Random Order)")
    plt.plot(sizes, bst_balanced_delete_times, marker='s', label="BST (Balanced Order)")
    plt.plot(sizes, sorted_set_delete_times, marker='^', label="SortedSet")
    plt.xlabel("Input Size")
    plt.ylabel("Deletion Time (ms)")
    plt.title("Deletion Time Comparison")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("graph.png", dpi=300)
    plt.show()

results = run_experiment([10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000])
save_results_csv(results)
plot_results(results)
