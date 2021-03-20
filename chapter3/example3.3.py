# n = 10
# while n >= -10:
#   if n == 0:
#     break
#   inv = 1.0 / n
#   print(inv)
#   n -= 1
  ###################
n = 10
while n >= -10:
  if n == 0:
    n -= 1 #이거 없으면 무한루프
    continue
  inv = 1.0 / n
  print(inv)
  n -= 1