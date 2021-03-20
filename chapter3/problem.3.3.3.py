natural = int(input("Input natural number : "))

for i in range(2, natural+1):
  for j in range(2, i+1):
    if i != j and i%j == 0:
      break
    else :
      print(i)
      break
