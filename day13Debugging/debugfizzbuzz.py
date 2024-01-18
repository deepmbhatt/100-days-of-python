#Here if the entered value is divisible by 3 it prints Fizz or if by 5 then BUzz if both then FizzBuzz
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)