d = [{'name':'Todd','phone':'555-1414','email':'todd@mail.net'},
{'name':'Helga','phone':'555-1618','email':'helga@mail.net'},
{'name':'LJ','phone':'555-2718','email':'lj@mail.net'}]

#전화번호가 8로 끝나는 사용자 이름을 출력하라

# for dic in d: #for i in [1,2,3]
#     # for j, k in i.items():
#         # d[i].values()
#     s = dic['phone'] 
#     if s[-1] == '8':
#         print(dic['name'])   

#이메일이 없는 사용자 이름을 출력하라
# for dic2 in d:
#     if dic2['email'] == None:
#         print(dic2['name'])

#사용자 이름을 입력하면 전화번호, 이메일을 출력하라
#이름이 없으면 '이름이 없습니다.'라는 메시지를 출력하라
find = False
user_name = input('Input the user name : ')
for dic3 in d:
    if dic3['name'] == user_name:
        print(dic3.values())
        find = True #exit() -> 사용x
        break
if not find :
    print("이름이 없습니다.")
        