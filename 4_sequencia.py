""""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

"""

def sequencia_a(n):
  return 2 * n - 1

def sequencia_b(n):
  return 2 ** n

def sequencia_c(n):
  return n ** 2

def sequencia_d(n):
  return (2 * n) ** 2

def sequencia_e(n):
  if n <= 2:
    return 1
  else:
    return sequencia_e(n - 1) + sequencia_e(n - 2)

def sequencia_f(n):
  if n == 1:
    return 2
  elif n == 2:
    return 10
  else:
    return sequencia_f(n - 1) + 1

# Testando as sequências
print("a) 1, 3, 5, 7,", sequencia_a(5))
print("b) 2, 4, 8, 16, 32, 64,", sequencia_b(7))
print("c) 0, 1, 4, 9, 16, 25, 36,", sequencia_c(8))
print("d) 4, 16, 36, 64,", sequencia_d(5))
print("e) 1, 1, 2, 3, 5, 8,", sequencia_e(7))
print("f) 2, 10, 12, 16, 17, 18, 19,", sequencia_f(8))