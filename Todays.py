def is_palindrome(string):
  # Remove spaces and convert to lowercase for uniformity
  cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
  # Check if the string is equal to its reverse
  return cleaned_string == cleaned_string[::-1]

# Example usage
if __name__ == "__main__":
  test_string = input("Enter a string to check if it's a palindrome: ")
  if is_palindrome(test_string):
    print("The string is a palindrome.")
  else:
    print("The string is not a palindrome.")