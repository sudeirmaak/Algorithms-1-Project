import time
import random
import matplotlib.pyplot as plt
import pandas as pd
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort

def generate_random_array(size, min_val=1, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]

def measure_time(sort_function, arr, runs=5):
    total_time = 0
    for _ in range(runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        total_time += (end_time - start_time) * 1000 
    return total_time / runs 

if __name__ == "__main__":
    sizes = [5, 10, 25, 50, 100, 250, 500, 1000, 5000, 10000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    
    times = {name: [] for name in algorithms}

    print("\n=== Sorting Algorithm Performance (ms) ===")
    print(f"{'Size':<10}{'Bubble Sort':<15}{'Insertion Sort':<15}{'Merge Sort':<15}{'Quick Sort':<15}")
    print("=" * 65)

    for size in sizes:
        arr = generate_random_array(size)
        row = f"{size:<10}"
        
        for name, func in algorithms.items():
            time_taken = measure_time(func, arr)
            times[name].append(time_taken)
            row += f"{time_taken:<15.2f}"
        
        print(row)

    df = pd.DataFrame(times, index=sizes)
    df.index.name = "Input Size"
    df.to_csv("sorting_results.csv")

    for name, time_list in times.items():
        plt.plot(sizes, time_list, label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    plt.title("Sorting Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.savefig("sorting_performance.png")
    plt.show()


