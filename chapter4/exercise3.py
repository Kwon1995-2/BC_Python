import random
pick = set()
while len(pick) < 6:
    n = random.randint(1, 45)
    if n not in pick: #같은 수 중복 빼버림 -> 집합은 중복x -> 없으면 죽음
        pick.add(n)
print(pick)
print(sorted(pick))