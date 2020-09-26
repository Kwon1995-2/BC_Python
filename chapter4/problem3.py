"""3명 이상의 친구 이름 리스트를 작성하고
insert()로 맨 앞에 새로운 친구 추가
insert()로 3번째 위치에 새로운 친구 추가
append()로 마지막에 친구추가
"""
friend = ["A","B","C"]
friend.insert(0,"D") #
friend.insert(3,"E")
print(friend)
friend.insert(100, "X") #append와 비슷한 기능
friend.append('a')
print(friend)

# numli = [1,2,3]
# numli.insert(1,17)
# print(numli)
# numli.append(4)
# numli.append(5)
# numli.append(6)
# numli.insert(3,25)
# del(numli[0])
# numli.pop(0)
# print(numli)