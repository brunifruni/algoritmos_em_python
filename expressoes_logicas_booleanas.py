x = 10
y = 1
res = not x > y
print (res)
# na ordem de precedencia primeiro vai ser a relação e depois o not
####
x = 10
y = 1
z = 5.5
res = (x > y) and ( z== y) #true and false = false
print (res)
####
x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x #1.55
#res true or not false and true
#res=true or true and true
#res= true or true
#res = true
print (res)
