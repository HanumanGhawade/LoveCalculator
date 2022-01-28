you_name = input('Enter your name\n').lower()
her_name = input('Enter Her name\n').lower()

t1 = you_name.count('t')
r1 = you_name.count('r')
u1 = you_name.count('u')
e1 = you_name.count('e')
true1 = t1+r1+u1+e1
t2 = her_name.count('t')
r2 = her_name.count('r')
u2 = her_name.count('u')
e2 = her_name.count('e')
true2 = t2+r2+u2+e2
true = true1 + true2

l1 = you_name.count('l')
o1 = you_name.count('o')
v1 = you_name.count('v')
e1 = you_name.count('e')
love1 = t1+r1+u1+e1
l2 = her_name.count('l')
o2 = her_name.count('o')
v2 = her_name.count('v')
e2 = her_name.count('e')
love2 = t2+r2+u2+e2
love = love1 + love2
true_love = str(true) + str(love)
print("your love score is ", true_love)

