#!/bin/python

import os

class InvalidInputError(Exception):
  def __init__(self, message="InvalidInputError: You have made an invaild entry"):
    super().__init__(message)

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

def factorial(num):
  if num == 0:
    return 1
  elif num < 0:
    raise InvalidInputError(f"InvalidInputError: '{num}' is less than zero")
  return factorial(num-1) * num

user_continue = "y"

while user_continue.lower() == "y":
  try:
    num = int(input("Enter a number: "))
    print(factorial(num))
    user_continue = input("Do you want to continue (y/n): ").strip().lower()

    if user_continue not in ["y", "n"]:
      raise InvalidInputError

    if user_continue == "y":
      clear_screen()
  except InvalidInputError as IIE:
    print(IIE)
  except ValueError as VE:
    clear_screen()
    print("Invalid input:", VE)
