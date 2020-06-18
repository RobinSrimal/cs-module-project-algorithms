'''
Input: an integer
Returns: an integer
'''

# recursion to find all possible sums: create an array of 1s with the length of n, then find all possible 
# contractions of the 1s. store number of possible combinations of subsets in dictionary




def eating_cookies(n):
    # Your code here

    lookup = {0:1, 1:1, 2:2, 3:4}

    
    for i in range(n+1):

        if i in lookup:

            continue

        else:

            lookup[i] = lookup[i-1] + lookup[i-2] +  lookup[i-3]

    
    return lookup[n]

  

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
