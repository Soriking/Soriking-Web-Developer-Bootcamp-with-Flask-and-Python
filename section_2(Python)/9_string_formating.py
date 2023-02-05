name='Bob'
print(f'Hello, {name}')

name='Ralf'
print(f'Hello, {name}')

#---------------------------

n='Sohrab'
greeting='Hello,{}'
with_name= greeting.format(n)
print(with_name)
with_name_2=greeting.format('David')
print(with_name_2)

#----------------------------
phrase='Hello,{}. Today is {}.'
print(phrase.format('World','Monday'))
