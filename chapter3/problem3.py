"""사용자로부터 이수한 학점을 입력 받는다. 
학점이 40학점 미만이면 "1학년입니다."를 출력
40이상 80미만이면, "2학년입니다." 출력
학점이 80이상이면, "졸업반입니다." 출력"""

score = int(input("Enter the score : "))

if score < 40 :
    print("1학년입니다.")
elif score >= 40 and score < 80 :
    print("2학년입니다.")
else :
    print("졸업반입니다.")
 
