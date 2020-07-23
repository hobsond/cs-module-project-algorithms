'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # iterate threw the array
    # and keep note if the value im at has been seen be fore 
    # and return the number that has only been seen once 
    y = {}
    for i in range(len(arr)):
        if arr[i] not in y:
            y.update({arr[i]:0})
        else:
            y.pop(arr[i])
    for k,v in y.items():
        return k




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")