n = int(input("Enter a number: "))

# Check if the number is a Fibonacci number
def pertence_a_fibonacci(n):
  sequence = [0,1]
  a,b = sequence
  while b < n:
    a, b = b, a + b
    sequence.append(b)

  print(f'Sequencia: {sequence}')
  return a == n

# Print the result
if pertence_a_fibonacci(n):
  print(f"{n} pertence à sequência de Fibonacci.")
else:
  print(f"{n} não pertence à sequência de Fibonacci.")


