# Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.
# An element is considered a peak if it is greater than both its left and right neighbors.
# It is guaranteed that the first and last elements are lower than all others.


### Solution:

# the question doesn't ask for highest peak, any peak works 
a = [20, 120, 30, 15, 25, 24, 22]
b = a[0]
def peak(a):
    left, right = 0, len(a)-1
    # we use an updated binary search
    while left < right:    #program biases over rightmost peak. for left ones, flip the condition
        mid = (left + right)//2
        if a[mid] > a[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left

c = peak(a)
print(a[c])
    