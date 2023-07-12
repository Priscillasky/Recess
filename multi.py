import time
import threading
import multiprocessing

def task(seconds):
    print(f"Running task {seconds} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name} to complete")
    print(f"Task started. Running for {seconds} seconds.")
    time.sleep(seconds)
    print("Task completed.")

# Multithreading example
def run_with_threads():
    durations = [1, 2, 3]  # Different durations for each thread

    threads = []
    for duration in durations:
        thread = threading.Thread(target=task, args=(duration,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Multiprocessing example
def run_with_processes():
    durations = [1, 2, 3]  # Different durations for each process

    processes = []
    for duration in durations:
        process = multiprocessing.Process(target=task, args=(duration,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Running the examples
print("Running with threads:")
run_with_threads()

print("\nRunning with processes:")
if __name__ == '__main__':
    multiprocessing.freeze_support()
    run_with_processes()

