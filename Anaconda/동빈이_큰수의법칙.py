#!/usr/bin/env python
# coding: utf-8

# In[1]:


N, M, K = map(int, input("자연수 3개 입력>>>").split())
print(N, M, K)


# In[21]:


#동빈이의 큰 수의 법칙
import copy

def findsec(arr):
    cpy = copy.deepcopy(arr)
    del cpy[arr.index(max(arr))]
    return max(cpy)

result = 0
# N : N개의 리스트, M : 총 더할 횟수, K : 특정 인덱스 수가 연속해서 더해질 횟수
N, M, K = map(int, input("자연수 3개 입력>>>").split())
# N개 만큼 자연수 입력 --> N개만 입력받도록 보완 필요
arr = [int(x) for x in input("%d개의 자연수 입력>>>"%N).split()]
# print(arr)

maxcnt = M//K # K는 항상 M보다 작거나 같다.
seccnt = M%K

result += max(arr)*maxcnt*K
# print("디버깅", max(arr), maxcnt)  
result += findsec(arr)*seccnt
# print("디버깅", findsec(arr), seccnt)

print(result)

