#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_value = prices[0]
  max_value = prices[len(prices) - 1]
  
  min_index = 0
  max_index = len(prices) - 1
  for i in range(1, len(prices)):
    if prices[i] < min_value and max_index > i:
      min_index = i
      min_value = prices[i]
    elif prices[i] > max_value and min_index < i:
      max_index = i
      max_value = prices[i]

  return max_value - min_value


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

