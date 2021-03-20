height = {'Jun':174,'Kim':170,'Lee':165}
# print(height)
# test = {}
# print(test)
# print("Kim" in height) #대소문자 구분
# print(height["Kim"])
# print(height["Lee"])
# height['Ihm']=168
# print(height)
# height['Lee']=180
# print(height)
# del(height['Ihm'])
# print(height)
# print(height.get('Lee'))
print(height.keys())
print(height.values())
print(height.items())
height['Ihm']=168
dict_keys = height.keys()
keys_list = list(dict_keys)
print(keys_list)
height.pop('Ihm')
print(height)
height.clear()
print(height)