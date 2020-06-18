'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here

#     output  = []

#     #non_zeros = 0

#     for number in arr:

#         if number == 0:

#             output.append(number)
        
#         else:

#             output.insert(0,number)

#             #non_zeros += 1

#     return output

def moving_zeroes(arr):

    switch = True 

    while switch:

        counter = 0

        for i in range(len(arr) - 1):

            if arr[i] == 0 and arr[i+1] != 0:

                arr[i], arr[i+1] = arr[i+1], arr[i]

                counter += 1

        if counter == 0:

            switch = False
    
    return arr










if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")