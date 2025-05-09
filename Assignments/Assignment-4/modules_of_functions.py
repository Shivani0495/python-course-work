def spy_numbers():
  return '''
  **Spy Numbers**

  n = int(input("Enter Number: "))
  sum_digits = 0
  prod_digits = 1
  temp = n
  while temp > 0:
      digit = temp % 10
      sum_digits += digit
      prod_digits *= digit
      temp //= 10
  if sum_digits == prod_digits:
      print("Spy Number")
  else:
      print("Not a Spy Number")
  ==========================================
  Testcase-1:
  Enter Number: 1124
  output:
  Spy Number
  ------------------------------------------
  Testcase-2:
  Enter Number: 1234
  output:
  Not a Spy Number
  ===========================================
  '''

def sum_of_digits():
  return '''
  **Sum of digits**

  n = int(input("Enter Number: "))
  sum = 0
  while n > 0:
      sum += n % 10
      n //= 10
  print(sum)
  ==========================================
  Testcase-1:
  Enter Number: 1234
  output:
  10
  ------------------------------------------
  Testcase-2:
  Enter Number: 567
  output:
  18
  ===========================================
  '''

def product_of_digits():
  return '''
  **product of digits**

  n = int(input("Enter Number: "))
  prod = 1
  while n > 0:
      prod *= n % 10
      n //= 10
  print(prod)
  ==========================================
  Testcase-1:
  Enter Number: 1234
  output:
  24
  ------------------------------------------
  Testcase-2:
  Enter Number: 567
  output:
  210
  ===========================================
  '''

def count_digits_in_a_number():
  return '''
  **count digits in a number**

  n = int(input("Enter Number: "))
  count = 0
  while n > 0:
      n //= 10
      count += 1
  print(count)
  ==========================================
  Testcase-1:
  Enter Number: 1234
  output:
  4
  ------------------------------------------
  Testcase-2:
  Enter Number: 98765
  output:
  5
  ===========================================
  '''

def check_if_a_number_is_a_perfect_square():
  return '''
  **check if a number is a perfect square**

  import math
  n = int(input("Enter Number: "))
  root = math.isqrt(n)
  if root * root == n:
      print("Perfect Square")
  else:
      print("Not a Perfect Square")
  ==========================================
  Testcase-1:
  Enter Number: 49
  output:
  Perfect Square
  ------------------------------------------
  Testcase-2:
  Enter Number: 50
  output:
  Not a Perfect Square
  ===========================================
  '''

def find_prime_factors_of_a_number():
  return '''
  **Find prime factors of a number**

  n = int(input("Enter Number: "))
  i = 2
  while i <= n:
      if n % i == 0:
          print(i, end=" ")
          n //= i
      else:
          i += 1
  print()
  ==========================================
  Testcase-1:
  Enter Number: 60
  output:
  2 2 3 5
  ------------------------------------------
  Testcase-2:
  Enter Number: 100
  output:
  2 2 5 5
  ===========================================
  '''

def count_number_of_prime_digits_in_a_number():
  return '''
  **count number of prime digits in a number**

  n = int(input("Enter Number: "))
  prime_digits = [2, 3, 5, 7]
  count = 0
  while n > 0:
      digit = n % 10
      if digit in prime_digits:
          count += 1
      n //= 10
  print(count)
  ==========================================
  Testcase-1:
  Enter Number: 2357
  output:
  4
  ------------------------------------------
  Testcase-2:
  Enter Number: 1234567890
  output:
  4
  ===========================================
  '''

def sum_of_square_of_first_n_natural_numbers():
  return '''
  **sum of square of first N natural numbers**

  n = int(input("Enter N: "))
  sum_squares = n * (n + 1) * (2 * n + 1) // 6
  print(sum_squares)
  ==========================================
  Testcase-1:
  Enter N: 3
  output:
  14
  ------------------------------------------
  Testcase-2:
  Enter N: 5
  output:
  55
  ===========================================
  '''

def sum_of_digits_of_factorial_of_a_number():
  return '''
  **sum of digits of factorial of a number**

  import math
  n = int(input("Enter Number: "))
  fact = math.factorial(n)
  sum_digits = sum(int(d) for d in str(fact))
  print(sum_digits)
  ==========================================
  Testcase-1:
  Enter Number: 5
  output:
  3
  ------------------------------------------
  Testcase-2:
  Enter Number: 10
  output:
  27
  ===========================================
  '''

def count_zero_digits_in_a_number():
  return '''
  **count zero digits in a number**

  n = int(input("Enter Number: "))
  count = 0
  while n > 0:
      if n % 10 == 0:
          count += 1
      n //= 10
  print(count)
  ==========================================
  Testcase-1:
  Enter Number: 10020
  output:
  2
  ------------------------------------------
  Testcase-2:
  Enter Number: 7001
  output:
  2
  ===========================================
  '''

def find_transpose_of_a_matrice():
  return '''
  **Find transpose of a matrice**

  rows = int(input("Enter number of rows: "))
  cols = int(input("Enter number of columns: "))
  matrix = []
  print("Enter matrix:")
  for i in range(rows):
      matrix.append(list(map(int, input().split())))
  transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
  print("Transpose:")
  for row in transpose:
      print(*row)
  ==========================================
  Testcase-1:
  Enter number of rows: 2
  Enter number of columns: 2
  Enter matrix:
  1 2
  3 4
  output:
  Transpose:
  1 3
  2 4
  ------------------------------------------
  Testcase-2:
  Enter number of rows: 2
  Enter number of columns: 3
  Enter matrix:
  1 2 3
  4 5 6
  output:
  Transpose:
  1 4
  2 5
  3 6
  ===========================================
  '''
def subtraction_of_two_matrices():
  return '''
  **Subtraction of two matrices**

  rows = int(input("Enter number of rows: "))
  cols = int(input("Enter number of columns: "))
  print("Enter first matrix:")
  matrix1 = [list(map(int, input().split())) for _ in range(rows)]
  print("Enter second matrix:")
  matrix2 = [list(map(int, input().split())) for _ in range(rows)]
  result = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]
  print("Subtraction:")
  for row in result:
      print(*row)
  ==========================================
  Testcase-1:
  Enter number of rows: 2
  Enter number of columns: 2
  Enter first matrix:
  1 2
  3 4
  Enter second matrix:
  4 3
  2 1
  output:
  -3 -1
  1 3
  ------------------------------------------
  Testcase-2:
  Enter number of rows: 2
  Enter number of columns: 3
  Enter first matrix:
  5 6 7
  8 9 10
  Enter second matrix:
  1 2 3
  4 5 6
  output:
  4 4 4
  4 4 4
  ===========================================
  '''

def number_divisible_by_5():
  return '''
  **Given number divisible by 5**

  n = int(input("Enter Number: "))
  if n % 5 == 0:
      print("Divisible by 5")
  else:
      print("Not divisible by 5")
  ==========================================
  Testcase-1:
  Enter Number: 25
  output:
  Divisible by 5
  ------------------------------------------
  Testcase-2:
  Enter Number: 23
  output:
  Not divisible by 5
  ===========================================
  '''

def area_of_circle():
  return '''
  **Area of a circle**

  import math
  r = float(input("Enter radius: "))
  area = math.pi * r * r
  print(area)
  ==========================================
  Testcase-1:
  Enter radius: 2
  output:
  12.566370614359172
  ------------------------------------------
  Testcase-2:
  Enter radius: 3.5
  output:
  38.48451000647496
  ===========================================
  '''
def area_of_triangle():
  return '''
  **Area of a triangle**

  b = float(input("Enter base: "))
  h = float(input("Enter height: "))
  area = 0.5 * b * h
  print(area)
  ==========================================
  Testcase-1:
  Enter base: 4
  Enter height: 5
  output:
  10.0
  ------------------------------------------
  Testcase-2:
  Enter base: 6
  Enter height: 8
  output:
  24.0
  ===========================================
  '''

def area_of_square():
  return '''
  **Area of a square**

  side = float(input("Enter side length: "))
  area = side * side
  print(area)
  ==========================================
  Testcase-1:
  Enter side length: 5
  output:
  25.0
  ------------------------------------------
  Testcase-2:
  Enter side length: 7.5
  output:
  56.25
  ===========================================
  '''
def repeated_word_in_string():
  return '''
  **Repeated word in a string**

  s = input("Enter string: ")
  words = s.split()
  counts = {}
  for word in words:
      counts[word] = counts.get(word, 0) + 1
  print("Repeated words:")
  for word, count in counts.items():
      if count > 1:
          print(word, "->", count)
  ==========================================
  Testcase-1:
  Enter string: this is a test this is only a test
  output:
  this -> 2
  is -> 2
  a -> 2
  test -> 2
  ------------------------------------------
  Testcase-2:
  Enter string: hello world hello
  output:
  hello -> 2
  ===========================================
  '''
def hcf_lcm_of_two_numbers():
  return '''
  **HCF & LCM of 2 numbers**

  import math
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  hcf = math.gcd(a, b)
  lcm = abs(a * b) // hcf
  print("HCF:", hcf)
  print("LCM:", lcm)
  ==========================================
  Testcase-1:
  Enter first number: 12
  Enter second number: 18
  output:
  HCF: 6
  LCM: 36
  ------------------------------------------
  Testcase-2:
  Enter first number: 5
  Enter second number: 7
  output:
  HCF: 1
  LCM: 35
  ===========================================
  '''
def gcd_lcm_of_two_numbers():
  return '''
  **GCD & LCM of 2 numbers**

  import math
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  gcd = math.gcd(a, b)
  lcm = abs(a * b) // gcd
  print("GCD:", gcd)
  print("LCM:", lcm)
  ==========================================
  Testcase-1:
  Enter first number: 8
  Enter second number: 32
  output:
  GCD: 8
  LCM: 32
  ------------------------------------------
  Testcase-2:
  Enter first number: 10
  Enter second number: 15
  output:
  GCD: 5
  LCM: 30
  ===========================================
  '''
def reverse_of_number():
  return '''
  **Reverse of a number**

  n = int(input("Enter Number: "))
  rev = 0
  while n > 0:
      rev = rev * 10 + n % 10
      n = n // 10
  print(rev)
  ==========================================
  Testcase-1:
  Enter Number: 1234
  output:
  4321
  ------------------------------------------
  Testcase-2:
  Enter Number: 560
  output:
  65
  ===========================================
  '''


