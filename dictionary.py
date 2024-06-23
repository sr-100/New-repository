dic={'name':'kani','ID':202}
print(dic)
print(type(dic))
#replacing
dic['name']='chairmakani'
print(dic)
dic.update({'degree':'M.E','role':'director'})
print(dic)
print(len(dic))
print(dic.keys())
print(dic.values())
print(dic.items())
print('my name is:',dic['name'])
print('I have completed:',dic.get('degree'))
del dic['ID']
print(dic)
dic.pop('degree')
print(dic)
#dic.remove()
print(dic)
dic.clear()
print(dic)
#list into dictionary
l1=['role','salary']
l2=['director','100000']
print(dict(zip(l1,l2)))
#set
s={1,3,25,10,'red'}
print(type(s))
print(len(s))
s.add(20)
print(s)
s.update([9,78])
print(s)
#delete
s.remove(25)
print(s)
s.discard(34)
print(s)
s.pop()
print(s)
print(s)
#
s.discard([30,50,60])
print(s)

