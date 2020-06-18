#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here


  options = [['rock'], ['paper'], ['scissors']]

  if n == 0:

    return [[]]

  if n == 1:

    return options

  output = []

  for result in rock_paper_scissors(n-1):

    for option in options:

      output.append(result + option)

  return output





  



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')