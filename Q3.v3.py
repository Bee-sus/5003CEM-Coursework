import random
import threading
import time


def gen_num():
    # Function to generate 100 random numbers ranging from 0 to 10000
    # Add slight computational work to ensure measurable time
    result = []
    for _ in range(100):
        num = random.randint(0, 10000)
        # Add minimal computation to make timing more reliable
        num = num * 2 // 2  # Simple operation that doesn't change the result
        result.append(num)
    return result


def multithreaded():
    # Generate 3 different sets of random numbers using multithreading
    # Creates 3 separate threads, one for each set
    results = []
    threads = []
    thread_times = {'start_times': [], 'end_times': []}
    lock = threading.Lock()

    # Acts as a way to tell each thread what to do which is generate the numbers then append it
    def thread_tasks():
        # Record when this thread starts
        thread_start = time.perf_counter_ns()
        with lock:
            thread_times['start_times'].append(thread_start)

        result = gen_num()

        # Record when this thread ends
        thread_end = time.perf_counter_ns()
        with lock:
            thread_times['end_times'].append(thread_end)
            results.append(result)

    # Create and start 3 threads
    for i in range(3):
        thread = threading.Thread(target=thread_tasks)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Calculate T: time from first thread start to last thread end
    earliest_start = min(thread_times['start_times'])
    latest_end = max(thread_times['end_times'])
    T = latest_end - earliest_start

    return T, results


def non_multithreaded():
    # Generate 3 different sets of random numbers sequentially
    results = []

    # Record start time
    start_time = time.perf_counter_ns()

    # Generate 3 sets sequentially
    for i in range(3):
        result = gen_num()
        results.append(result)

    # Record end time
    end_time = time.perf_counter_ns()

    return end_time - start_time, results


def main():
    print("Round-by-Round Performance Comparison:")
    print("|" + "=" * 7 + "|" + "=" * 27 + "|" + "=" * 29 + "|" + "=" * 17 + "|")
    print("| Round | Multithreading Time (ns)  | Non-Multithreading Time (ns) | Difference (ns) |")
    print("|" + "=" * 7 + "|" + "=" * 27 + "|" + "=" * 29 + "|" + "=" * 17 + "|")

    # Store results for all rounds
    multi_times = []
    non_multi_times = []

    # Perform 10 rounds of testing
    for round_num in range(1, 11):
        # Test multithreaded execution
        multi_time, multi_results = multithreaded()
        multi_times.append(multi_time)

        # Test sequential execution
        non_multi_time, non_multi_results = non_multithreaded()
        non_multi_times.append(non_multi_time)

        # Calculate difference (positive means multithreading is slower)
        difference = multi_time - non_multi_time

        # Display results for this round
        print(
            f"|   {round_num:2d}  |        {multi_time:10d}        |          {non_multi_time:10d}           |    {difference:9d}    |")

    print("|" + "=" * 7 + "|" + "=" * 27 + "|" + "=" * 29 + "|" + "=" * 17 + "|")

    # Calculate summary statistics
    multi_total = sum(multi_times)
    non_multi_total = sum(non_multi_times)
    multi_average = multi_total / 10
    non_multi_average = non_multi_total / 10
    total_difference = multi_total - non_multi_total
    avg_difference = multi_average - non_multi_average

    print("\nSummary of Results:")
    print("|" + "=" * 14 + "|" + "=" * 27 + "|" + "=" * 29 + "|" + "=" * 17 + "|")
    print("|    Metric    | Multithreading (ns)       | Non-Multithreading (ns)     | Difference (ns) |")
    print("|" + "=" * 14 + "|" + "=" * 27 + "|" + "=" * 29 + "|" + "=" * 17 + "|")
    print(
        f"| Total Time   |        {multi_total:10d}         |        {non_multi_total:10d}           |   {total_difference:11d}   |")
    print(
        f"| Average Time |        {multi_average:10.1f}         |        {non_multi_average:10.1f}           |   {avg_difference:11.1f}   |")
    print("|" + "=" * 14 + "|" + "=" * 27 + "|" + "=" * 29 + "|" + "=" * 17 + "|")


if __name__ == "__main__":
    main()