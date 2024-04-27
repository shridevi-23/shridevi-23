apple=[5,10,30,40]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])
#print(apple[4])
print("for iteration via access")
for i in apple:
    print(i)
print("after changed")
apple[1]=-100
print(apple)
apple[2]=(300,400)
print(apple)
print(apple[-1])
apple[3]=500,600,700
print(apple)
apple[1:4]=(-10,-20,-30)
print(apple)