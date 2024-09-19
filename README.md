# CPs-API-Load-test

### Key Elements: Simplicity, Ease of Use, Clean Useable Results

Use the app.py to load test any of your endpoint deployed anywhere. Eg. ElasticBeanstalk, CloudRun, Lambda etc. 

The objective is to help the developed undertand what performance to expect from the API and how much it can be pushed.

This librery is primarily used to fine tune configs on auto-sclaing and load balancing.

### All you need to know: Only three variables
```
concurrent_load = 2000  # Number of requests that are active at any time
test_duration = 2 * 60 * 60  # Test duration in seconds (2 hours)
complete_all_load_before_dumping_new_load = True  # Flag to control the request strategy
```
##### concurrent_load explained
```
concurrent_load -> Set this to the number of requests/users you want to simulate hitting the endpoint
```
##### test_duration explained
```
test_duration -> Set this to a number in seconds, you want to run the test for
```
##### complete_all_load_before_dumping_new_load explained
```
complete_all_load_before_dumping_new_load -> True means a step loading function.
Say concurrent_load is set to 500, The system will make 500 requests in parallel.
Wait for all the 500 to complete. Then the system will make another 500 requests in parallel.
So if you look at the number of open requests:
It will spike up from 0 to 500 and ramp down to 0 slowly.
Then spike up from 0 to 500 again and ramp down to 0 slowly.
Thus will repeat.
```
```
complete_all_load_before_dumping_new_load -> False means at any point in time the system will maintain N number of open requests.
Say concurrent_load is set to 500, The system will make 500 requests in parallel.
Then as each request completes with a respinse, a new requets will be opened immediately.
So if you look at the number of open requests:
It will constantly be at a number close to what concurrent_load is set to.
```

### Results
As the test runs results will be dumped into a CSV by name assigned to test_name variable.

Here is a snippet of what the results will look like.
(Step loading with 50 concurrent requests)

| Time (s) | Successful Requests (per sec) | Unsuccessful Requests (per sec) | Average Response Time (s) | Total Requests Sent | Total Requests Completed | Total Successful Requests | Total Unsuccessful Requests |
|----------|-------------------------------|---------------------------------|---------------------------|---------------------|--------------------------|---------------------------|-----------------------------|
| 0        | 0                             | 0                               | 0                         | 0                   | 0                        | 0                         | 0                           |
| 1.01     | 0                             | 0                               | 0                         | 50                  | 0                        | 0                         | 0                           |
| 2.01     | 27                            | 0                               | 1.739                     | 50                  | 27                       | 27                        | 0                           |
| 3.02     | 1                             | 0                               | 1.749                     | 50                  | 28                       | 28                        | 0                           |
| 4.02     | 22                            | 0                               | 2.473                     | 50                  | 50                       | 50                        | 0                           |
| 5.03     | 0                             | 0                               | 2.473                     | 100                 | 50                       | 50                        | 0                           |
| 6.04     | 1                             | 0                               | 2.453                     | 100                 | 51                       | 51                        | 0                           |
| 7.04     | 47                            | 0                               | 2.208                     | 100                 | 98                       | 98                        | 0                           |
| 8.04     | 2                             | 0                               | 2.226                     | 100                 | 100                      | 100                       | 0                           |
| 9.05     | 0                             | 0                               | 2.226                     | 150                 | 100                      | 100                       | 0                           |
| 10.06    | 0                             | 0                               | 2.226                     | 150                 | 100                      | 100                       | 0                           |
| 11.06    | 27                            | 0                               | 2.135                     | 150                 | 127                      | 127                       | 0                           |
| 12.07    | 8                             | 0                               | 2.155                     | 150                 | 135                      | 135                       | 0                           |
| 13.07    | 14                            | 0                               | 2.295                     | 150                 | 149                      | 149                       | 0                           |
| 14.08    | 1                             | 0                               | 2.313                     | 150                 | 150                      | 150                       | 0                           |
| 15.08    | 0                             | 0                               | 2.313                     | 200                 | 150                      | 150                       | 0                           |
| 16.09    | 0                             | 0                               | 2.313                     | 200                 | 150                      | 150                       | 0                           |
| 17.09    | 36                            | 0                               | 2.212                     | 200                 | 186                      | 186                       | 0                           |
| 18.1     | 14                            | 0                               | 2.216                     | 200                 | 200                      | 200                       | 0                           |
| 19.11    | 0                             | 1                               | 2.216                     | 250                 | 201                      | 200                       | 1                           |
| 20.11    | 11                            | 0                               | 2.183                     | 250                 | 212                      | 211                       | 1                           |
| 21.11    | 36                            | 0                               | 2.158                     | 250                 | 248                      | 247                       | 1                           |
| 22.12    | 2                             | 0                               | 2.167                     | 250                 | 250                      | 249                       | 1                           |
| 23.12    | 0                             | 0                               | 2.167                     | 300                 | 250                      | 249                       | 1                           |
