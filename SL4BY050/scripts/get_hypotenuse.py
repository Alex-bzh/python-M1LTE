#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
#   libraries
#
import math


#
#   user functions
#
def hypotenuse(x, y):
  """Calculates the hypotenuse thanks to
  the Pythagorean theorem in a right triangle.
    
  Keyword arguments:
  x -- first cathetus
  y -- second cathetus
  """
  square = (x ** 2) + (y ** 2)
  hypotenuse = math.sqrt(square)

  # Rounded to two digits from the decimal point
  return round(hypotenuse, 2)

def main():

  while True:
    try:
      # Writes the argument to standard output,
      # then reads a line from input and returns it as a string.
      x = int(input("Quelle est la mesure de la première cathète (en cm) ?\n"))
      y = int(input("Quelle est la mesure de la seconde cathète (en cm) ?\n"))
    except ValueError:
      print("Veuillez entrer un chiffre")
    else:
      print(f"La mesure de l’hypoténuse vaut {hypotenuse(x, y)} cm.")
      break

#
#   main procedure
#
if __name__ == "__main__":

  main()
