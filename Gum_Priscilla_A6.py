# Show a context manager for file handling that automatically opens and closes a file
import sqlite3
import multiprocessing
import threading
import time


class FileHanler():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, except_tb, exc_value):
        self.file.close()


with FileHanler("gum.txt", "w") as f:
    f.write('I love front end.\n')

print(f.closed)


# Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.


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

# Shows a context manager for managing a database connection.


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


# database name
db_name = "Priscilla_Gum.db"

# Using the context manager
with DatabaseConnection(db_name) as db:
    cursor = db.cursor()
    # Create the "people" table if it doesn't exist
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)")

    # Insert a sample user
    cursor.execute("INSERT INTO people (name) VALUES ('Gum Priscillag')")
    db.commit()

    # Performing database operations on people
    # The first line of code creates a cursor object that allows you to execute SQL statements and fetch
    # results from the database.
    cursor.execute("SELECT * FROM people")
    results = cursor.fetchall()
    for row in results:
        print(row)

        print(row)
