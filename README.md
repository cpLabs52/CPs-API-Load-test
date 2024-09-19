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

```
A. complete_all_load_before_dumping_new_load = True
Step Loading with concurrent_load = 50 requests/users
```
| Time (s) | Successful Requests (per sec) | Unsuccessful Requests (per sec) | Average Response Time (s) | Total Requests Sent | Total Requests Completed | Open Requests | Total Successful Requests | Total Unsuccessful Requests |
|----------|-------------------------------|---------------------------------|---------------------------|---------------------|--------------------------|---------------|---------------------------|-----------------------------|
| 0.0      | 0                             | 0                               | 0                         | 2                   | 0                        | 1             | 0                         | 0                           |
| 1.0      | 0                             | 0                               | 0                         | 50                  | 0                        | 50            | 0                         | 0                           |
| 2.01     | 18                            | 0                               | 1.968                     | 50                  | 18                       | 32            | 18                        | 0                           |
| 3.01     | 18                            | 0                               | 2.124                     | 50                  | 36                       | 14            | 36                        | 0                           |
| 4.02     | 14                            | 0                               | 2.557                     | 50                  | 50                       | 0             | 50                        | 0                           |
| 5.02     | 0                             | 0                               | 2.557                     | 100                 | 50                       | 50            | 50                        | 0                           |
| 6.02     | 0                             | 0                               | 2.557                     | 100                 | 50                       | 50            | 50                        | 0                           |
| 7.03     | 0                             | 0                               | 2.557                     | 100                 | 50                       | 50            | 50                        | 0                           |
| 8.03     | 0                             | 0                               | 2.557                     | 100                 | 50                       | 50            | 50                        | 0                           |
| 9.04     | 5                             | 0                               | 2.688                     | 100                 | 55                       | 45            | 55                        | 0                           |
| 10.04    | 42                            | 0                               | 3.502                     | 100                 | 97                       | 3             | 97                        | 0                           |
| 11.05    | 3                             | 0                               | 3.559                     | 100                 | 100                      | 0             | 100                       | 0                           |
| 12.06    | 0                             | 0                               | 3.559                     | 150                 | 100                      | 50            | 100                       | 0                           |
| 13.06    | 0                             | 0                               | 3.559                     | 150                 | 100                      | 50            | 100                       | 0                           |
| 14.07    | 0                             | 0                               | 3.559                     | 150                 | 100                      | 50            | 100                       | 0                           |
| 15.07    | 50                            | 0                               | 3.462                     | 150                 | 150                      | 0             | 150                       | 0                           |
| 16.08    | 0                             | 0                               | 3.462                     | 200                 | 150                      | 50            | 150                       | 0                           |
| 17.09    | 0                             | 0                               | 3.462                     | 200                 | 150                      | 50            | 150                       | 0                           |
| 18.09    | 0                             | 0                               | 3.462                     | 200                 | 150                      | 50            | 150                       | 0                           |
| 19.1     | 0                             | 0                               | 3.462                     | 200                 | 150                      | 50            | 150                       | 0                           |
| 20.11    | 34                            | 0                               | 3.548                     | 200                 | 184                      | 16            | 184                       | 0                           |
| 21.11    | 13                            | 0                               | 3.621                     | 200                 | 198                      | 2             | 198                       | 0                           |
| 22.12    | 2                             | 0                               | 3.639                     | 200                 | 200                      | 0             | 200                       | 0                           |
| 23.13    | 0                             | 0                               | 3.639                     | 250                 | 200                      | 50            | 200                       | 0                           |
| 24.13    | 0                             | 0                               | 3.639                     | 250                 | 200                      | 50            | 200                       | 0                           |
| 25.14    | 28                            | 0                               | 3.517                     | 250                 | 228                      | 22            | 228                       | 0                           |
| 26.15    | 21                            | 0                               | 3.483                     | 250                 | 249                      | 1             | 249                       | 0                           |
| 27.15    | 0                             | 0                               | 3.483                     | 250                 | 249                      | 1             | 249                       | 0                           |
| 28.16    | 1                             | 0                               | 3.488                     | 250                 | 250                      | 0             | 250                       | 0                           |
| 29.17    | 0                             | 0                               | 3.488                     | 300                 | 250                      | 50            | 250                       | 0                           |
| 30.18    | 0                             | 0                               | 3.488                     | 300                 | 250                      | 50            | 250                       | 0                           |
| 31.18    | 0                             | 0                               | 3.488                     | 300                 | 250                      | 50            | 250                       | 0                           |
| 32.18    | 45                            | 0                               | 3.512                     | 300                 | 295                      | 5             | 295                       | 0                           |
```
B. complete_all_load_before_dumping_new_load = False
Maintain open concurrent_load = 50 requests/users
```
| Time (s) | Successful Requests (per sec) | Unsuccessful Requests (per sec) | Average Response Time (s) | Total Requests Sent | Total Requests Completed | Open Requests | Total Successful Requests | Total Unsuccessful Requests |
|----------|-------------------------------|---------------------------------|---------------------------|---------------------|--------------------------|---------------|---------------------------|-----------------------------|
| 0        | 0                             | 0                               | 0                         | 1                   | 0                        | 1             | 0                         | 0                           |
| 1.01     | 0                             | 0                               | 0                         | 50                  | 0                        | 50            | 0                         | 0                           |
| 2.01     | 0                             | 0                               | 0                         | 50                  | 0                        | 50            | 0                         | 0                           |
| 3.02     | 0                             | 0                               | 0                         | 50                  | 0                        | 50            | 0                         | 0                           |
| 4.02     | 0                             | 0                               | 0                         | 50                  | 0                        | 50            | 0                         | 0                           |
| 5.03     | 27                            | 0                               | 4.744                     | 50                  | 27                       | 23            | 27                        | 0                           |
| 6.04     | 23                            | 0                               | 5.043                     | 77                  | 50                       | 27            | 50                        | 0                           |
| 7.04     | 12                            | 0                               | 4.374                     | 100                 | 62                       | 38            | 62                        | 0                           |
| 8.05     | 22                            | 0                               | 3.731                     | 112                 | 84                       | 28            | 84                        | 0                           |
| 9.05     | 25                            | 0                               | 3.323                     | 134                 | 109                      | 25            | 109                       | 0                           |
| 10.06    | 13                            | 0                               | 3.155                     | 160                 | 122                      | 38            | 122                       | 0                           |
| 11.06    | 25                            | 0                               | 2.927                     | 173                 | 148                      | 25            | 148                       | 0                           |
| 12.07    | 17                            | 0                               | 2.825                     | 198                 | 165                      | 33            | 165                       | 0                           |
| 13.07    | 22                            | 0                               | 2.705                     | 215                 | 187                      | 28            | 187                       | 0                           |
| 14.08    | 22                            | 0                               | 2.614                     | 237                 | 209                      | 28            | 209                       | 0                           |
| 15.08    | 17                            | 0                               | 2.543                     | 262                 | 229                      | 33            | 229                       | 0                           |
| 16.09    | 22                            | 0                               | 2.48                      | 279                 | 251                      | 28            | 251                       | 0                           |
| 17.09    | 19                            | 0                               | 2.433                     | 303                 | 272                      | 32            | 271                       | 0                           |
| 18.1     | 18                            | 0                               | 2.399                     | 322                 | 290                      | 32            | 290                       | 0                           |
| 19.11    | 28                            | 0                               | 2.36                      | 340                 | 318                      | 22            | 318                       | 0                           |
| 20.11    | 12                            | 0                               | 2.342                     | 368                 | 330                      | 38            | 330                       | 0                           |
| 21.12    | 29                            | 0                               | 2.308                     | 380                 | 359                      | 21            | 359                       | 0                           |
| 22.13    | 13                            | 0                               | 2.305                     | 411                 | 372                      | 37            | 372                       | 0                           |
| 23.14    | 20                            | 0                               | 2.285                     | 430                 | 392                      | 37            | 392                       | 0                           |
| 24.15    | 17                            | 0                               | 2.289                     | 453                 | 409                      | 44            | 409                       | 0                           |
| 25.15    | 22                            | 0                               | 2.283                     | 468                 | 431                      | 37            | 431                       | 0                           |
| 26.16    | 10                            | 0                               | 2.287                     | 491                 | 441                      | 49            | 441                       | 0                           |
| 27.17    | 19                            | 0                               | 2.286                     | 500                 | 460                      | 38            | 460                       | 0                           |
| 28.17    | 20                            | 0                               | 2.288                     | 525                 | 480                      | 44            | 480                       | 0                           |
| 29.18    | 0                             | 0                               | 2.288                     | 530                 | 480                      | 50            | 480                       | 0                           |
| 30.18    | 42                            | 0                               | 2.308                     | 562                 | 522                      | 40            | 522                       | 0                           |
| 31.19    | 8                             | 0                               | 2.309                     | 580                 | 530                      | 50            | 530                       | 0                           |
| 32.2     | 0                             | 0                               | 2.309                     | 580                 | 530                      | 50            | 530                       | 0                           |
| 33.2     | 0                             | 0                               | 2.309                     | 580                 | 530                      | 50            | 530                       | 0                           |
| 34.21    | 21                            | 0                               | 2.356                     | 601                 | 551                      | 50            | 551                       | 0                           |
| 35.21    | 21                            | 0                               | 2.436                     | 622                 | 572                      | 50            | 572                       | 0                           |
| 36.22    | 10                            | 0                               | 2.458                     | 632                 | 582                      | 50            | 582                       | 0                           |
| 37.22    | 19                            | 0                               | 2.451                     | 651                 | 601                      | 50            | 601                       | 0                           |
| 38.23    | 0                             | 0                               | 2.451                     | 651                 | 601                      | 50            | 601                       | 0                           |
| 39.24    | 0                             | 0                               | 2.451                     | 651                 | 601                      | 50            | 601                       | 0                           |
| 40.24    | 25                            | 0                               | 2.516                     | 676                 | 626                      | 50            | 626                       | 0                           |
| 41.25    | 6                             | 0                               | 2.533                     | 682                 | 632                      | 50            | 632                       | 0                           |
| 42.25    | 19                            | 0                               | 2.605                     | 683                 | 651                      | 32            | 651                       | 0                           |
| 43.25    | 9                             | 0                               | 2.609                     | 710                 | 660                      | 50            | 660                       | 0                           |
| 44.26    | 14                            | 0                               | 2.618                     | 724                 | 674                      | 50            | 674                       | 0                           |
| 45.26    | 19                            | 0                               | 2.627                     | 743                 | 693                      | 50            | 693                       | 0                           |
| 46.26    | 27                            | 0                               | 2.612                     | 767                 | 720                      | 47            | 720                       | 0                           |
| 47.27    | 14                            | 0                               | 2.6                       | 784                 | 734                      | 50            | 734                       | 0                           |
| 48.27    | 19                            | 0                               | 2.583                     | 803                 | 753                      | 50            | 753                       | 0                           |
| 49.28    | 14                            | 0                               | 2.576                     | 817                 | 767                      | 50            | 767                       | 0                           |
| 50.29    | 0                             | 0                               | 2.576                     | 817                 | 767                      | 50            | 767                       | 0                           |
| 51.29    | 14                            | 0                               | 2.578                     | 831                 | 781                      | 50            | 781                       | 0                           |
| 52.3     | 14                            | 0                               | 2.574                     | 845                 | 795                      | 50            | 795                       | 0                           |
| 53.3     | 23                            | 0                               | 2.634                     | 868                 | 818                      | 50            | 818                       | 0                           |
| 54.31    | 10                            | 0                               | 2.631                     | 877                 | 828                      | 49            | 828                       | 0                           |
| 55.31    | 27                            | 0                               | 2.618                     | 906                 | 856                      | 50            | 856                       | 0                           |
| 56.32    | 19                            | 0                               | 2.61                      | 925                 | 875                      | 50            | 875                       | 0                           |
| 57.32    | 4                             | 0                               | 2.609                     | 929                 | 879                      | 50            | 879                       | 0                           |
| 58.32    | 41                            | 0                               | 2.587                     | 970                 | 920                      | 50            | 920                       | 0                           |
| 59.33    | 7                             | 0                               | 2.582                     | 977                 | 927                      | 50            | 927                       | 0                           |
| 60.33    | 26                            | 0                               | 2.561                     | 999                 | 953                      | 44            | 953                       | 0                           |
| 61.33    | 15                            | 0                               | 2.557                     | 1018                | 968                      | 50            | 968                       | 0                           |
| 62.34    | 12                            | 0                               | 2.555                     | 1023                | 980                      | 43            | 980                       | 0                           |
| 63.35    | 31                            | 0                               | 2.545                     | 1061                | 1011                     | 50            | 1011                      | 0                           |
| 64.35    | 10                            | 0                               | 2.541                     | 1071                | 1021                     | 50            | 1021                      | 0                           |
| 65.36    | 0                             | 0                               | 2.541                     | 1071                | 1021                     | 50            | 1021                      | 0                           |
| 66.36    | 8                             | 0                               | 2.544                     | 1079                | 1029                     | 50            | 1029                      | 0                           |
| 67.37    | 40                            | 0                               | 2.573                     | 1119                | 1069                     | 50            | 1069                      | 0                           |
| 68.38    | 5                             | 0                               | 2.571                     | 1124                | 1074                     | 50            | 1074                      | 0                           |
| 69.38    | 0                             | 0                               | 2.571                     | 1124                | 1074                     | 50            | 1074                      | 0                           |
| 70.39    | 40                            | 0                               | 2.569                     | 1162                | 1114                     | 48            | 1114                      | 0                           |
| 71.39    | 8                             | 0                               | 2.572                     | 1173                | 1123                     | 50            | 1123                      | 0                           |
| 72.4     | 25                            | 0                               | 2.555                     | 1198                | 1148                     | 50            | 1148                      | 0                           |
| 73.4     | 17                            | 0                               | 2.557                     | 1215                | 1165                     | 50            | 1165                      | 0                           |
| 74.4     | 8                             | 0                               | 2.558                     | 1223                | 1173                     | 50            | 1173                      | 0                           |
| 75.41    | 33                            | 0                               | 2.552                     | 1254                | 1206                     | 48            | 1206                      | 0                           |
| 76.42    | 15                            | 0                               | 2.549                     | 1271                | 1221                     | 50            | 1221                      | 0                           |
| 77.47    | 26                            | 0                               | 2.533                     | 1278                | 1248                     | 29            | 1248                      | 0                           |
| 78.47    | 18                            | 0                               | 2.524                     | 1313                | 1266                     | 47            | 1266                      | 0                           |
| 79.47    | 28                            | 0                               | 2.511                     | 1339                | 1294                     | 45            | 1294                      | 0                           |
| 80.48    | 19                            | 0                               | 2.5                       | 1362                | 1313                     | 49            | 1313                      | 0                           |
| 81.49    | 15                            | 0                               | 2.491                     | 1378                | 1328                     | 50            | 1328                      | 0                           |
| 82.49    | 10                            | 0                               | 2.489                     | 1388                | 1338                     | 50            | 1338                      | 0                           |
| 83.5     | 27                            | 0                               | 2.487                     | 1413                | 1365                     | 48            | 1365                      | 0                           |
| 84.5     | 23                            | 0                               | 2.484                     | 1438                | 1388                     | 50            | 1388                      | 0                           |
| 85.51    | 20                            | 0                               | 2.474                     | 1454                | 1408                     | 46            | 1408                      | 0                           |
| 86.52    | 27                            | 0                               | 2.462                     | 1481                | 1437                     | 45            | 1436                      | 0                           |
| 87.52    | 16                            | 0                               | 2.453                     | 1503                | 1453                     | 50            | 1453                      | 0                           |
| 88.53    | 27                            | 0                               | 2.442                     | 1526                | 1480                     | 46            | 1480                      | 0                           |
| 89.54    | 22                            | 0                               | 2.432                     | 1549                | 1502                     | 47            | 1502                      | 0                           |
| 90.54    | 21                            | 0                               | 2.422                     | 1573                | 1524                     | 49            | 1524                      | 0                           |
| 91.55    | 22                            | 0                               | 2.414                     | 1593                | 1546                     | 47            | 1546                      | 0                           |
| 92.56    | 20                            | 0                               | 2.406                     | 1615                | 1566                     | 49            | 1566                      | 0                           |
| 93.56    | 20                            | 0                               | 2.399                     | 1635                | 1587                     | 48            | 1587                      | 0                           |
| 94.57    | 5                             | 0                               | 2.398                     | 1643                | 1593                     | 50            | 1593                      | 0                           |
| 95.58    | 31                            | 0                               | 2.397                     | 1670                | 1624                     | 46            | 1624                      | 0                           |
| 96.59    | 17                            | 0                               | 2.396                     | 1691                | 1641                     | 50            | 1641                      | 0                           |
| 97.6     | 20                            | 0                               | 2.388                     | 1713                | 1663                     | 50            | 1663                      | 0                           |
| 98.61    | 25                            | 0                               | 2.381                     | 1736                | 1688                     | 48            | 1688                      | 0                           |
| 99.62    | 4                             | 0                               | 2.381                     | 1742                | 1692                     | 50            | 1692                      | 0                           |


