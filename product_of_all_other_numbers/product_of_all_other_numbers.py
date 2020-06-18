'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

    length = len(arr)

    total_product = 1 

    index_zeros = []

    for index,number in enumerate(arr):

        if number == 0:

            index_zeros.append(index)

        else:

            total_product = total_product*number

    
    if len(index_zeros) == 1:

        arr = [0]*length

        arr[index_zeros[0]] = total_product

        return arr
    
    elif len(index_zeros) > 1:

        return [0]*length


    else:

        return [total_product/number for number in arr]

    




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
