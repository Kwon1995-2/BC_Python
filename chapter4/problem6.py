days ={'January':31, 'Febury':28,'March':31,'April':30, 'May':31,'June':30,'July':31,'August':31, 'September':30, 'October':31,'November':30,'December':31}
#사용자가 월을 입력하면 해당 월에 일수를 출력하라
#month = input("Input Month : " )
#print(days[input("Input Month : " )])
#print(days[month])
# days_list = list(days.keys())
# days_list2 = list(days.values())
# for i in range(0, len(days_list)):
#     if month == days_list[i]:
#         print(days_list2[i])

#알파벳 순서로 모든 월을 출력하라
# srt_days = []
# srt_days = list(days.keys())
# print(sorted(srt_days))

#일수가 31인 월을 모두 출력하라
# kv_li = days.items()
# for i, j in kv_li :
#     if j == 31:
#         print(i)

#월의 일수를 기준으로 오름차순으로 쌍을 출력하라
print(sorted(days.items(), key=lambda k : k[1]))
#http://blog.naver.com/PostView.nhn?blogId=msyang59&logNo=220627524714
#k[1]은 values를 기준으로 하겠다는 것


#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라
key = input("Input Month : " )
kv_li2 = days.items()
for i, j in kv_li2:
    if i[:3] == key:
        print(j)
        break


