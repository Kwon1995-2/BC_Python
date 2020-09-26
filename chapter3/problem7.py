''' 플레이어가 처음에 $50을 가짐
동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 
맞추면 $9을 따고 틀리면 $10을 잃는다.
플레이어가 돈을 모두 잃거나 $100이 되면 게임을 종료'''

from random import  randint
budget = 50

# while budget >=0 and budget <100:
#     coin = randint(1,2)
#     fortune = int(input("앞면(1) or 뒷면(2) : "))
#     if coin == fortune:
#         budget += 9
#         if budget >= 100:
#             budget = 100
#             print("You win! Your budget is ",budget)
#         else : 
#             print("You get! current budget is ",budget)
#     else :
#         budget -= 10
#         if budget <= 0:
#             budget = 0
#             print("You lose.. Your budget is ",budget)
#         else:
#             print("You're wrong! current budget is",budget)


while 0 < budget < 100:
    coin = randint(1,2)
    fortune = input("앞면(1) or 뒷면(2) : ")
    if not fortune in ("1", "2"):
        print("Invalid!")
        #continue
        break

    fortune = int(fortune)
    if coin == fortune:
        budget += 9
        print("You win! Your budget is ",budget)
    else :
        budget -= 10
        print("You lose.. Your budget is ",budget)
