The first brute force approach is to search entire space of possibilities:
that is do the binary search in 0,10^4 as start and end points
​
Now the second approach is more inticrate how can you find the boundaries using binary search?
start at any give position as 0,1
if the target element is smaller than element at end
you can do binary search between start and end
if the target element is greater than 1 than double your end position
and make start as end