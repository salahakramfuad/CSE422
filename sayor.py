def check_even_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# Example usage
if __name__ == "__main__":
  num = int(input("Enter a number: "))
  result = check_even_odd(num)
  print(f"The number {num} is {result}.")