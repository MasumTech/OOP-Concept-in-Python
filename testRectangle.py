from rectangle import Rectangle


r1 = Rectangle(20,10)

r2 = Rectangle(20,10)

r3 = r1


test1 = r1==r2

test2 = r1==r3



print("r1==r2?", test1)

print("r1==r3?",test2)

print("---------")

print("r1!=r2?", r1!=r2)
print("r1!=r3?", r1!=r3)



''''''''''

print("r1.width", r1.width)

print("r1.height", r2.height)

print("r1.getWidth()=", r1.getWidth())

print("r1.getArea()=", r1.getArea())


print("----------------")


print("r2.width", r1.width)

print("r2.height", r2.height)


print("r2.getWidth()=", r2.getWidth())

print("r2.getArea()=", r2.getArea())
'''''''''''''''
