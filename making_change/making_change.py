#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here

  lookup = {0:1,1:1,2:1,3:1,4:1,5:2}

  for i in range(amount+1):

    if i < 5:

      continue

    elif 4 < i < 10:

      lookup[i] = lookup[i-1] + lookup[i-5]

    elif 9 < i < 25:

      lookup[i] = lookup[i-1] + lookup[i-5] + lookup[i-10]

    elif 24 < i < 50:

      lookup[i] = lookup[i-1] + lookup[i-5] + lookup[i-10] + lookup[i-25]

    else:

      lookup[i] = lookup[i-1] + lookup[i-5] + lookup[i-10] + lookup[i-25] + lookup[i-50]

  return lookup[amount]




if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")