#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
  This script is a minimal example that uses the prerequisites
  expected of any program written in Python.
"""

#
# Libraries
#
import math

#
# User functions
#
def to_square_root(x):
  """Get the square root of a given number."""
  return math.sqrt(x)

def main():
  nb = input("Saisissez un nombre :\n")
  nb = int(nb)
  sq = to_square_root(nb)

  print(f"La racine carrée de {nb} est {sq}")

#
# Main procedure
#
if __name__ == '__main__':

  # call to 'main'
  main()
