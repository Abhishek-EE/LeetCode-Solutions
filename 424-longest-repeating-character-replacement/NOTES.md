You can break the problem into two small problems
1. Form  a set of all the characthers (max possible value is 26) O(N)
2. Traverse through all the characther and find the max occurence of the that specific charachter in the string
3. Finding the longest repeating sequence with charachter replacement for a specific letter in the string. This can be done using the simple sliding window approach. this is O(N)
​
Final time complextiy = 0(N)
Final extra space complexity = O(1)