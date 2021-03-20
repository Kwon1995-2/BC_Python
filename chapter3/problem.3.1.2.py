a, b, c = input().split()
if int(a) == 0:
  print("a can't be zero!")
else :
  D = int(b)**2 - 4*int(a)*int(c)
  if(D > 0):
    print("쌍근")
  elif(D < 0):
    print("허근")
  else :
    print("중근")
