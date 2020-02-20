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
      print(f'IIII: {i}')
    for k in range(i+1, len(prices)):
      print(f'I: {i}, K: {k}')
      if prices[k] > max_value and min_index < k:
        max_index = k
        max_value = prices[k]





  print(f'Final Min: {min_value}, Final Max: {max_value}')
  print(f'final Min index: {min_index}, Final Max Index: {max_index}')
  return max_value - min_value


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

