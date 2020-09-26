"""반복문과 조건문을 사용해 점수를 계속 입력 받아 90점 이상이면, A
80이상이면 B, 60점 이상이면 C, 40점이상이면 D, 39점 이하이면 F
출력
입력받는 점수가 음수일 때 종료"""

while 1:
    score = int(input("Input the score : "))
    if score >= 0 :
        if score >= 90 :
            print("A")
            continue
        elif score >= 80 :
            print("B")
            continue
        elif score >= 60 :
            print("C")
            continue
        elif score >= 40 :
            print("D")
            continue
        else :
            print("F")
            continue
    else :
        print("Enter the Positive!")
        break
