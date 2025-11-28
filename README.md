# VRPTW-ALNS

This repo provides a ALNS meta-heuristic to solve VRPTW (Vehicle Routing Problem with Time Windows), which is NP-hard. We also implement the SISRs (Slack Induction by String Removals) technique in `Jan Christiaens, Greet Vanden Berghe (2020) Slack Induction by String Removals for Vehicle Routing Problems. Transportation Science`, **which is proved to be a simple yet powerful heuristic for variants of VRP**. Experiments analysis can be found below.


## Numerical Experiments 

We provide a brief report of the numerical experiments. The results are obtained by running our code on Solomon benchmark instances. Column `Obj` indicates the objective value of our algorithm (which is measured by total distance), `#.T` shows the number of vehicles used in our solution, `CPU(s)` denotes the CPU time in seconds, `Gap BKS(%)` is the gap to the Best-Known Solution (BKS), `BKS #.T` is the number of vehicles used in the BKS, and `Note(#.T)` is the note, mainly the increase of vehicles compared with BKS. 

We may test our algorithm on more benchmarks in the future. As it's coded in pure Python, performance (running time) is somewhat terrible. We will try to fix that later. Analysis on running time verified a great time waste in destroy operators, with 0.07 s per action for 100 customer cases.

Total iteration Num is 20,000. The table display the best solution of 2-run.

|  Inst   |   Obj   | #.Truck  | CPU (s) | Gap to BKS | BKS #. Trucks | Note(#.T) |
| :-----: | :-----: | :------: | :-----: | :--------: | :-----------: | --------- |
|  c101   | 828.94  |    10    | 123.32  |     0      |      10       | 0         |
|  c102   | 828.94  |    10    | 499.45  |     0      |      10       | 0         |
|  c103   | 828.94  |    10    | 358.43  |    0.11    |      10       | 0         |
|  c104   | 825.65  |    10    |  363.1  |    0.1     |      10       | 0         |
|  c105   | 878.36  |    10    | 114.54  |    5.96    |      10       | 0         |
|  c106   | 852.95  |    10    | 252.34  |    2.9     |      10       | 0         |
|  c107   | 1027.16 |    10    |  70.22  |   23.91    |      10       | 0         |
|  c108   | 828.94  |    10    | 311.17  |     0      |      10       | 0         |
|  c109   | 828.94  |    10    | 365.59  |     0      |      10       | 0         |
|  c201   | 591.56  |    3     |  78.2   |     0      |       3       | 0         |
|  c202   |  688.1  |    3     | 218.44  |   16.32    |       3       | 0         |
|  c203   | 591.17  |    3     | 188.28  |     0      |       3       | 0         |
|  c204   |  590.6  |    3     | 184.38  |     0      |       3       | 0         |
|  c205   | 588.88  |    3     | 132.56  |     0      |       3       | 0         |
|  c206   | 588.49  |    3     | 175.25  |     0      |       3       | 0         |
|  c207   | 588.29  |    3     | 174.84  |     0      |       3       | 0         |
|  c208   | 588.32  |    3     |  129.8  |     0      |       3       | 0         |
|  r101   | 1831.62 |    20    | 557.62  |   10.95    |      19       | 1         |
|  r102   | 1548.41 |    17    |  742.3  |    4.19    |      17       | 0         |
|  r103   | 1258.71 |    15    | 630.89  |   -2.63    |      13       | 2         |
|  r104   | 1019.71 |    10    | 517.56  |    1.23    |       9       | 1         |
|  r105   | 1472.71 |    15    | 633.56  |    6.94    |      14       | 1         |
|  r106   | 1313.28 |    14    | 382.57  |    4.89    |      12       | 2         |
|  r107   | 1113.32 |    12    | 536.72  |    0.78    |      10       | 2         |
|  r108   | 960.71  |    10    | 508.37  |   -0.02    |       9       | 1         |
|  r109   | 1231.66 |    13    | 445.21  |    3.09    |      11       | 2         |
|  r110   | 1141.12 |    12    | 654.65  |    1.99    |      10       | 2         |
|  r111   | 1097.16 |    12    | 595.87  |    0.04    |      10       | 2         |
|  r112   | 1002.95 |    11    | 514.42  |    2.12    |       9       | 2         |
|  r201   | 1311.68 |    4     | 276.44  |    4.74    |       4       | 0         |
|  r202   | 1102.18 |    4     | 178.54  |   -7.51    |       3       | 1         |
|  r203   | 1011.96 |    3     | 247.48  |    7.71    |       3       | 0         |
|  r204   | 773.92  |    3     | 280.75  |   -6.25    |       2       | 1         |
|  r205   | 1075.37 |    3     | 176.62  |    8.14    |       3       | 0         |
|  r206   | 972.68  |    3     | 178.26  |    7.34    |       3       | 0         |
|  r207   |  834.8  |    3     | 145.92  |   -6.27    |       2       | 1         |
|  r208   | 729.03  |    3     | 295.12  |    0.3     |       2       | 1         |
|  r209   | 944.67  |    3     | 176.58  |    3.91    |       3       | 0         |
|  r210   | 975.34  |    3     | 250.43  |    3.83    |       3       | 0         |
|  r211   | 850.86  |    3     | 156.76  |   -3.93    |       2       | 1         |
|  rc101  | 1868.4  |    17    | 440.45  |    10.1    |      14       | 3         |
|  rc102  | 1539.85 |    14    | 687.45  |   -0.96    |      12       | 2         |
|  rc103  | 1288.57 |    12    |  514.8  |    2.13    |      11       | 1         |
|  rc104  | 1188.06 |    11    |  332.3  |    4.63    |      10       | 1         |
|  rc105  | 1641.12 |    16    | 701.88  |    0.72    |      13       | 3         |
|  rc106  | 1420.32 |    13    | 353.65  |   -0.31    |      11       | 2         |
|  rc107  | 1265.77 |    11    | 330.88  |    2.87    |      11       | 0         |
|  rc108  | 1184.41 |    11    | 332.99  |    3.91    |      10       | 1         |
|  rc201  | 1454.42 |    4     | 276.54  |    3.38    |       4       | 0         |
|  rc202  | 1231.73 |    4     | 267.42  |   -9.81    |       3       | 1         |
|  rc203  | 1091.99 |    3     | 170.58  |    4.04    |       3       | 0         |
|  rc204  | 853.05  |    3     | 177.96  |    6.84    |       3       | 0         |
|  rc205  | 1412.58 |    4     | 312.24  |    8.86    |       4       | 0         |
|  rc206  | 1139.45 |    4     | 183.76  |    -0.6    |       3       | 1         |
|  rc207  | 1096.83 |    3     | 213.23  |    3.36    |       3       | 0         |
|  rc208  | 874.44  |    3     | 283.56  |    5.59    |       3       | 0         |
| **AVG** | 1047.66 | **7.91** | 328.61  |  **2.49**  |     7.23      | **0.68**  |

We're conducting experiments on Gehring&Homberge dataset. The results are as follows:

Customer = 200, column indicate the average of all instances. 

| Inst  |   Obj   | #.Truck | CPU (s) | Gap to BKS | BKS #. Trucks | Note(#.T) |
| :---: | :-----: | :-----: | :-----: | :--------: | :-----------: | --------- |
|  C1   | 3020.75 |  19.7   | 1263.15 |    9.53    |     18.9      | 0.8+      |
|  C2   | 2021.50 |   6.8   | 644.37  |   10.46    |       6       | 0.8+      |
|  R1   | 4196.01 |  18.9   | 1359.25 |   16.01    |     18.2      | 0.7+      |
|  R2   | 3220.89 |   4.3   | 521.08  |   11.24    |       4       | 0.3+      |

Customer = 400 + , to be continued ... 


-----

## Report 

This repo incorporates some but not all features of SISRs and ALNS. We list them below.

**Destroy Operator:**

> 1. **Random Removal** ✅, Randomly remove some customers from current solution.
>
> 2. **String removal** ✅, including the string and split-string removal proposed in paper above. **The idea is to remove sufficient-enough, adjacent or geographically-close customers**, like multiple "strings", from current solution to produce new routes that are more likely to bring about improvement.

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202502051156972.png)

> Source: SISRs paper.

**Repair (Recreate) Operator:**

> 1. **Greedy Insertion with Blink** ✅ : which is very similar to Greedy Insertion, yet before insertion, customers to be inserted are sorted with respect to random, demand, (distance) far, close, increasing time window length, increasing time window start, and decreasing time window end.

**NOTES:**

1. To check the feasibility efficiently during repair process, the **Forward Time Slack** is implemented. (See `Martin W. P. Savelsbergh, (1992) The Vehicle Routing Problem with Time Windows: Minimizing Route Duration. ORSA Journal on Computing 4(2):146-154. http://dx.doi.org/10.1287/ijoc.4.2.146`)
2. Several initial solution construction method are implemented. The C-W saving is adopted. Further experiment is required.
   1. Solomon's Time-oriented Nearest Neighbor, in 1987 ✅
   2. Naive Construction: each customer with a route. ✅
   3. Clark & Wright Saving Heuristic, 1964. ✅
3. **Fleet Minimization approach**: We don't strictly follow the fleet minimization procedure in TS paper. Currently, we just randomly remove an entire route from the solution and try to recreate a brand new solution. This is proved to be a little bit helpful yet still much room to improve. 
4. Simulated Annealing has **NOT** been implemented yet.
5. Adaptive Weight Adjustment, which is commonly used in ALNS, has **NOT** been implemented yet.
6. Some SOTA heuristic like [PyVRP package](https://pyvrp.readthedocs.io/en/latest/) are provided. You just need to call it.
