'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # Loop through the array 
    for i in range(len(arr)):
        if arr[i] == 0:
            x = arr[i]
            arr.pop(i)
            arr.append(x)
            
    return arr
            
    # if that i is equal to zero
    # we pop that item 
    # and then append to the zero 

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")