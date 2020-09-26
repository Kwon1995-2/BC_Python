#숫자 맞추기 프로그램
'''1~100 사이의 난수를 만들고 사용자가 1~100 사이의 수를 
입력하여 맞춰라. 5회까지 맞추지 못하면 종료'''
# from random import randint #random에서 randint함수만 쓰겠다 명시
# secret_num = randint(1,100)
# #Input_num = int(input("Input between 1 and 100 : "))
# n = 0
# while n != 5:
#     Input_num = int(input("Input between 1 and 100 : "))
#     if secret_num == Input_num:
#         print("Right answer!")
#         break
#     else :
#         n = n + 1
#         if n == 5 :
#             print("Opportunity out! Answer is %d"%secret_num)
#             break
#         print("Try again")
#         continue
'''right answer '''
# from random import randint
# secret_num = randint(1,100)
# num_guesses = 0
# guess = 0
# while guess != secret_num and num_guesses <= 4 :
#     guess = int(input("Enter your guess (1-100):"))
#     num_guesses += 1
#     if guess < secret_num:
#         print('더 큽니다.', 5-num_guesses,'회 남았습니다.')
#     elif guess > secret_num:
#         print('더 작습니다.', 5-num_guesses,'회 남았습니다.')
#     else:
#         print("맞았습니다.")
# if num_guesses == 5 and guess != secret_num:
#     print("당신이 졌습니다. 정답은", secret_num, '입니다.')

