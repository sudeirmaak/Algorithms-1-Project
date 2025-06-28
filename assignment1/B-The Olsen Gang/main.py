import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def load_data(file1, file2):
    part1 = pd.read_csv(file1)  
    part2 = pd.read_csv(file2) 
    return part1, part2

def sort_file2(part2):
    return part2.sort_values(by=["Expiry Date", "PIN"]).reset_index(drop=True)

def merge_credit_card_numbers(part1, part2_sorted):
    if len(part1) != len(part2_sorted):
        raise ValueError("Mismatch in dataset sizes after sorting.")

    part1_cleaned = part1.iloc[:, 0].astype(str).str.replace(r"\*", "", regex=True)

    part2_last4 = part2_sorted["Credit Card Number"].astype(str).str[-4:]

    part1["Credit Card Number"] = part1_cleaned + part2_last4

    return part1

def match_cards(part1, part2_sorted):
    matched = []
    for i in range(len(part1)):
        combined_row = {**part2_sorted.iloc[i].to_dict(), "Credit Card Number": part1.iloc[i]["Credit Card Number"]}
        matched.append(combined_row)
    return pd.DataFrame(matched)

def empirical_test_and_graph(part1, part2):
    dataset_sizes = [500, 1000, 2500, 5000, 10000, 15000, 20000]
    log_linear_times = []
    linear_times = []
    
    sorted_part2 = sort_file2(part2)

    for size in dataset_sizes:
        part1_subset = part1.iloc[:size].copy()
        part2_subset = part2.iloc[:size].copy()

        start = time.time()
        sorted_part2_log = sort_file2(part2_subset.copy())  
        merge_credit_card_numbers(part1_subset.copy(), sorted_part2_log) 
        log_linear_times.append(time.time() - start)

        start = time.time()
        merge_credit_card_numbers(part1_subset.copy(), sorted_part2.iloc[:size])  
        linear_times.append(time.time() - start)

    results_df = pd.DataFrame({
        "Dataset Size": dataset_sizes,
        "Log-Linear Time (O(n log n))": log_linear_times,
        "Linear Time (O(n))": linear_times
    })
    results_df.to_csv("sorting_execution_times.csv", index=False)

    plt.figure(figsize=(10, 6))
    plt.plot(dataset_sizes, log_linear_times, label="Log-Linear Algorithm (O(n log n))", marker='o', linestyle='--', color='blue')
    plt.plot(dataset_sizes, linear_times, label="Linear Algorithm (O(n))", marker='o', linestyle='-', color='green')
    plt.title("Algorithm Runtime Comparison")
    plt.xlabel("Dataset Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("algorithm_runtime_comparison.png")
    plt.show()

if __name__ == "__main__":
    part1, part2 = load_data("carddump1.csv", "carddump2.csv")
    
    if len(part1) != 20000 or len(part2) != 20000:
        raise ValueError("Both input files must have exactly 20,000 records.")
    
    part2_sorted = sort_file2(part2)

    part1 = merge_credit_card_numbers(part1, part2_sorted)
    matched_data = match_cards(part1, part2_sorted)
    matched_data.to_csv("matched_data.csv", index=False)
    print(f"Matched data saved with {len(matched_data)} records.")
    
    print("Graph and table generated.")
    empirical_test_and_graph(part1, part2)
