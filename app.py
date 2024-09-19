import requests
import concurrent.futures
import time
import threading
import csv
from statistics import mean

API_URL = "<your_url>"
auth = "<your_auth>"

# Adjustable load variables
concurrent_load = 500  # Number of requests that are active at any time
test_duration = 2 * 60 * 60  # Test duration in seconds (2 hours)
complete_all_load_before_dumping_new_load = True  # Flag to control the request strategy

payload = {
  <your_payload>
}

# Tracking statistics
successful_requests = []
unsuccessful_requests = []
total_requests_sent = 0
total_requests_completed = 0

lock = threading.Lock()


def query(payload):
    """
    Function to send a POST request to the API with the provided payload.
    Tracks response time and whether the request was successful or unsuccessful.
    """
    global total_requests_sent, total_requests_completed
    try:
        with lock:
            total_requests_sent += 1  # Increment the total requests sent counter when request is submitted

        start_time = time.time()
        response = requests.post(API_URL, auth=auth, data=payload, timeout=90)
        end_time = time.time()

        elapsed_time = end_time - start_time  # Calculate response time

        with lock:
            if 200 <= response.status_code < 300:
                successful_requests.append((elapsed_time, time.time()))
            else:
                unsuccessful_requests.append((response.status_code, time.time()))
            total_requests_completed += 1  # Increment the total completed requests counter

        return response.status_code
    except requests.exceptions.RequestException as e:
        with lock:
            unsuccessful_requests.append((str(e), time.time()))
            total_requests_completed += 1  # Increment the total completed requests counter
        return None


def log_stats(start_time, test_name):
    """
    Function to log stats about requests per second and write them to a CSV file.
    The stats include:
    - Successful requests per second
    - Unsuccessful requests per second
    - Average response time of successful requests
    - Total requests sent, total completed requests, total successful, and unsuccessful requests
    - Number of open requests (difference between total sent and total completed)
    
    The CSV is named according to the 'test_name' parameter and is saved in the current directory.
    """
    csv_file = f"{test_name}.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers to CSV
        writer.writerow(["Time (s)", "Successful Requests (per sec)", "Unsuccessful Requests (per sec)", "Average Response Time (s)", "Total Requests Sent", "Total Requests Completed", "Open Requests", "Total Successful Requests", "Total Unsuccessful Requests"])
        
        while time.time() - start_time < test_duration:
            with lock:
                current_time = time.time()
                successes = [r for r in successful_requests if current_time - r[1] <= 1]
                failures = [r for r in unsuccessful_requests if current_time - r[1] <= 1]
                avg_response_time = mean([r[0] for r in successful_requests]) if successful_requests else 0
                total_success = len(successful_requests)
                total_failure = len(unsuccessful_requests)
                open_requests = total_requests_sent - total_requests_completed  # Calculate open requests

            # Print and log data for the current second
            print(f"Time: {current_time - start_time:.2f}s")
            print(f"Successful requests (per second): {len(successes)}")
            print(f"Unsuccessful requests (per second): {len(failures)}")
            print(f"Average response time: {avg_response_time:.3f}s")
            print(f"Total requests sent: {total_requests_sent}")
            print(f"Total requests completed: {total_requests_completed}")
            print(f"Open requests: {open_requests}")
            print(f"Total successful requests: {total_success}")
            print(f"Total unsuccessful requests: {total_failure}\n")

            # Write to CSV
            writer.writerow([round(current_time - start_time, 2), len(successes), len(failures), round(avg_response_time, 3), total_requests_sent, total_requests_completed, open_requests, total_success, total_failure])
            file.flush()  # Flush the data to disk to ensure it is written immediately

            time.sleep(1)  # Sleep for 1 second before next log


def stress_test(payload, load, test_name):
    """
    Function to perform a stress test by continuously sending requests to the API.
    The test runs for the specified duration (test_duration) with the provided load.
    Logs stats and writes them to a CSV file with the name 'test_name'.
    
    If complete_all_load_before_dumping_new_load is True:
        It sends a batch of `concurrent_load` requests, waits for all of them to complete, and then sends the next batch.
    
    If complete_all_load_before_dumping_new_load is False:
        It maintains a consistent number of open requests close to `concurrent_load` by sending new requests as previous ones complete.
    """
    start_time = time.time()
    
    # Start the logger thread to log stats every second
    log_thread = threading.Thread(target=log_stats, args=(start_time, test_name))
    log_thread.start()

    # Start sending requests with the specified load
    with concurrent.futures.ThreadPoolExecutor(max_workers=load) as executor:
        if complete_all_load_before_dumping_new_load:
            # Complete all requests before sending new ones (current behavior)
            while time.time() - start_time < test_duration:
                futures = [executor.submit(query, payload) for _ in range(load)]
                for future in concurrent.futures.as_completed(futures):
                    future.result()  # Process result (to avoid leaving futures unprocessed)
                time.sleep(1)  # Can be used to control pacing
        else:
            # Maintain a constant number of open requests (new behavior)
            open_requests = set()
            while time.time() - start_time < test_duration:
                # Remove completed futures
                completed = {f for f in open_requests if f.done()}
                open_requests -= completed
                
                # Add new requests to maintain the load
                while len(open_requests) < load:
                    future = executor.submit(query, payload)
                    open_requests.add(future)
                
                time.sleep(1)  # Can be used to control pacing

    log_thread.join()


# Run the stress test
test_name = "500_step_load"  # Modify this to any desired name (this will be the result CSV's name)
stress_test(payload, concurrent_load, test_name)
