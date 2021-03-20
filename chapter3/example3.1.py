# score = int(input("정수 입력:"))
# if score >= 90 :
#   print("성적 - A")
#   print("장학금 수여")
########################
# age_0 = 22
# age_1 = 18
# age = int(input('your age? ')) 
# if age_1 <= age <= age_0 : #age<=age_0 and age>=age_1
#   print("Your age is between 18 and 22")
########################
# score = int(input("정수 입력:"))
# if score >= 90:
#   res = "pass"
# else :
#   res = "fail"
# print(res)
# res = 'pass' if score >= 90 else 'fail'
# print(res)
########################
# n = int(input("type iint number : "))
# print("positive") if n>0 else print("negative") if n<0 else print('0')
# print("negative") if n<0 else print("0") if n == 0 else print("positive")
# if n>0:
#   print("positive")
# elif n<0:
#   print("negative")
# else :
#   print('0')

age = 12
if age < 4:
  price = 0
elif age < 18:
  price = 5
elif age < 65:
  price = 10
else :
  price = 5
print("Your admission cost is $"+str(price)+".")